from application import app, db
from flask import redirect, render_template, request, url_for
from application.models import Pokemon

@app.route("/", methods=["GET"])
def pokemon_index():
    return render_template("list.html", pokemonlist = Pokemon.query.all())

@app.route("/", methods=["POST"])
def pokemon_create():
    p = Pokemon(request.form.get("name"), int(request.form.get("cp")), int(request.form.get("iv")))
    db.session().add(p)
    db.session().commit()
    return redirect(url_for("pokemon_index"))

@app.route("/new/")
def pokemon_form():
    return render_template("new.html")

