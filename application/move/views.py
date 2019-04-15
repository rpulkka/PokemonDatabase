from flask import render_template, request, redirect, url_for

from application import app, db, login_required
from application.move.models import Move
from application.move.forms import MoveForm, MoveUpdateForm

from flask_login import current_user

@app.route("/new_move", methods=["GET"])
@login_required(role="USER")
def move_form():
    return render_template("new_move.html", form = MoveForm())

@app.route("/new_move", methods=["POST"])
@login_required(role="USER")
def move_create():
    form = MoveForm(request.form)

    if not form.validate():
        return render_template("new_move.html", form = form)

    answer = request.form.get("chargeMove")

    if answer is 'y':
        answer = True
    else:
        answer = False

    m = Move(request.form.get("name"), int(request.form.get("damage")), answer, int(request.form.get("bars")))
    db.session().add(m)
    db.session().commit()
    return redirect(url_for("index"))

@app.route("/update_move/<move_id>", methods=["GET"])
@login_required(role="USER")
def move_update_form(move_id):
    move = Move.query.get(move_id)
    return render_template("update_move.html", form = MoveUpdateForm(), move = move)

@app.route("/update_move/<move_id>", methods=["POST"])
@login_required(role="USER")
def move_update(move_id):
    form = MoveUpdateForm(request.form)

    if not form.validate():
        return render_template("update_move.html", form = form)

    if answer is 'y':
        answer = True
    else:
        answer = False

    m = Move.query.get(move_id)
    m.name = request.form.get("name")
    m.damage = int(request.form.get("damage"))
    m.chargeMove = answer
    m.bars = int(request.form.get("bars"))

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