from flask import render_template, request, redirect, url_for

from application import app, db, login_required
from application.move.models import Move
from application.move.forms import MoveForm, MoveUpdateForm
from application.type.models import Type

import enum
from sqlalchemy import Integer, Enum

from flask_login import current_user

@app.route("/new_move", methods=["GET"])
@login_required(role="USER")
def move_form():
    form = MoveForm()

    form.firsttype.choices = [(t.value, t.name) for t in Type]

    return render_template("new_move.html", form = form)

@app.route("/new_move", methods=["POST"])
@login_required(role="USER")
def move_create():
    form = MoveForm(request.form)

    form.firsttype.choices = [(t.value, t.name) for t in Type]

    if not form.validate():
        return render_template("new_move.html", form = form)

    answer = request.form.get("chargemove")

    #if answer is 'y':
    #    answer = True
    #else:
    #    answer = False

    firsttypenum = request.form.get("firsttype")

    m = Move(request.form.get("name"), int(request.form.get("damage")), int(request.form.get("chargemove")), int(request.form.get("bars")), firsttypenum)
    db.session().add(m)
    db.session().commit()
    return redirect(url_for("index"))

@app.route("/update_move/<move_id>", methods=["GET"])
@login_required(role="USER")
def move_update_form(move_id):
    move = Move.query.get(move_id)
    form = MoveUpdateForm()
    form.firsttype.choices = [(t.value, t.name) for t in Type]
    return render_template("update_move.html", form = form, move = move)

@app.route("/update_move/<move_id>", methods=["POST"])
@login_required(role="USER")
def move_update(move_id):
    form = MoveUpdateForm(request.form)

    form.firsttype.choices = [(t.value, t.name) for t in Type]

    if not form.validate():
        return render_template("update_move.html", form = form)

    #if answer is 'y':
    #    answer = True
    #else:
    #    answer = False

    firsttypenum = request.form.get("firsttype")

    m = Move.query.get(move_id)
    m.name = request.form.get("name")
    m.damage = int(request.form.get("damage"))
    m.chargemove = int(request.form.get("chargemove"))
    m.bars = int(request.form.get("bars"))
    m.first_type_id = firsttypenum

    db.session().commit()
    return redirect(url_for("index"))

@app.route("/delete_move/<move_id>/", methods=["POST"])
@login_required(role="USER")
def move_delete(move_id):
    m = Move.query.get(move_id)
    m.destructor()
    Move.query.filter_by(id=move_id).delete()
    db.session().commit()
    return redirect(url_for("index"))