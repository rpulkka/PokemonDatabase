from flask import render_template, request, redirect, url_for

from application import app, db, login_required
from application.move.models import Move
from application.move.forms import MoveForm
from application.type.models import Type

import enum
from sqlalchemy import Integer, Enum

from flask_login import current_user

@app.route("/new_move", methods=["GET"])
@login_required(role="USER")
def move_form():
    form = MoveForm()

    form.firsttype.choices = [(t.value, t.name) for t in Type]

    return render_template("move/new_move.html", form = form)

@app.route("/new_move", methods=["POST"])
@login_required(role="USER")
def move_create():
    form = MoveForm(request.form)

    form.firsttype.choices = [(t.value, t.name) for t in Type]

    if not form.validate():
        return render_template("move/new_move.html", form = form)

    answer = request.form.get("chargemove")

    if answer is 'y':
        answer = 1
    else:
        answer = 0

    firsttypenum = request.form.get("firsttype")

    m = Move(request.form.get("name"), int(request.form.get("damage")), answer, int(request.form.get("bars")), firsttypenum)
    db.session().add(m)
    db.session().commit()
    return redirect(url_for("index"))

@app.route("/move/<move_id>", methods=["GET"])
def move_view(move_id):
    move = Move.query.get(move_id)
    return render_template("move/view_move.html", move = move)

@app.route("/update_move/<move_id>", methods=["GET"])
@login_required(role="USER")
def move_update_form(move_id):
    move = Move.query.get(move_id)
    form = MoveForm()
    form.name.data = move.name
    form.damage.data = move.damage
    form.chargemove.data = move.chargemove
    form.bars.data = move.bars
    form.firsttype.choices = [(t.value, t.name) for t in Type]
    form.firsttype.data = move.first_type_id
    return render_template("move/update_move.html", form = form, move = move)

@app.route("/update_move/<move_id>", methods=["POST"])
@login_required(role="USER")
def move_update(move_id):
    form = MoveForm(request.form)

    form.firsttype.choices = [(t.value, t.name) for t in Type]

    if not form.validate():
        return render_template("move/update_move.html", form = form)

    answer = request.form.get("chargemove")

    if answer is 'y':
        answer = 1
    else:
        answer = 0

    firsttypenum = request.form.get("firsttype")

    m = Move.query.get(move_id)
    m.name = request.form.get("name")
    m.damage = int(request.form.get("damage"))
    m.chargemove = answer
    m.bars = int(request.form.get("bars"))
    m.first_type_id = firsttypenum

    db.session().commit()
    return redirect(url_for("index"))

@app.route("/delete_move/<move_id>/", methods=["POST"])
@login_required(role="USER")
def move_delete(move_id):
    m = Move.query.get(move_id)

    if m.canDelete(current_user.id):
        m.destructor()
        Move.query.filter_by(id=move_id).delete()
        db.session().commit()

    return redirect(url_for("index"))