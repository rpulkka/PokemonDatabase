from flask import render_template, request, redirect, url_for

from application import app, db
from application.move.models import Move
from application.move.forms import MoveForm, MoveUpdateForm

from flask_login import login_required, current_user

@app.route("/new_move", methods=["GET"])
@login_required
def move_form():
    return render_template("new_move.html", form = MoveForm())

@app.route("/new_move", methods=["POST"])
@login_required
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
@login_required
def move_update_form(move_id):
    move = Move.query.get(move_id)
    return render_template("update_move.html", form = MoveUpdateForm(), move = move)

@app.route("/delete_move/<move_id>/", methods=["POST"])
@login_required
def move_delete(move_id):
    Move.query.filter_by(id=move_id).delete()
    db.session().commit()
    return redirect(url_for("index"))