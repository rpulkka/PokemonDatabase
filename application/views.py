from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.models import Pokemon
from application.auth.models import User
from application.move.models import Move
from application.forms import PokemonForm, AccountForm, PokemonUpdateForm


@app.route("/", methods=["GET"])
def index():
    account = User.query
    return render_template("index.html", pokemonlist = Pokemon.query.all(), movelist = Move.query.all(), account = account, 
        highest_cp = Pokemon.find_highest_cp(), highest_iv = Pokemon.find_highest_iv())

@app.route("/new_pokemon", methods=["GET"])
@login_required(role="USER")
def pokemon_form():
    return render_template("new_pokemon.html", form = PokemonForm())

@app.route("/new_pokemon", methods=["POST"])
@login_required(role="USER")
def pokemon_create():
    form = PokemonForm(request.form)

    if not form.validate():
        return render_template("new_pokemon.html", form = form)

    p = Pokemon(request.form.get("name"), int(request.form.get("cp")), int(request.form.get("iv")), int(request.form.get("fastMove_id")), int(request.form.get("chargeMove_id")))
    p.account_id = current_user.id
    db.session().add(p)
    db.session().commit()
    return redirect(url_for("index"))

@app.route("/update_pokemon/<pokemon_id>", methods=["GET"])
@login_required(role="USER")
def pokemon_update_form(pokemon_id):
    pokemon = Pokemon.query.get(pokemon_id)
    return render_template("update_pokemon.html", form = PokemonUpdateForm(), pokemon = pokemon)

@app.route("/update_pokemon/<pokemon_id>", methods=["POST"])
@login_required(role="USER")
def pokemon_update(pokemon_id):
    form = PokemonUpdateForm(request.form)

    if not form.validate():
        return render_template("update_pokemon.html", form = form)

    p = Pokemon.query.get(pokemon_id)
    p.name = request.form.get("name")
    p.cp = request.form.get("cp")
    p.iv = request.form.get("iv")

    db.session().commit()
    return redirect(url_for("index"))

@app.route("/delete_pokemon/<pokemon_id>/", methods=["POST"])
@login_required(role="USER")
def pokemon_delete(pokemon_id):
    Pokemon.query.filter_by(id=pokemon_id).delete()
    db.session().commit()
    return redirect(url_for("index"))

@app.route("/new_account/", methods=["GET"])
def account_form():
    return render_template("new_account.html", form = AccountForm())

@app.route("/new_account", methods=["POST"])
def account_create():
    form = AccountForm(request.form)

    if not form.validate():
        return render_template("new_account.html", form = form)

    u = User(request.form.get("username"), request.form.get("username"), request.form.get("password"))
    db.session().add(u)
    db.session().commit()
    return redirect(url_for("index"))

