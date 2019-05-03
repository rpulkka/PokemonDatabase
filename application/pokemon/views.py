from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.pokemon.models import Pokemon
from application.auth.models import User
from application.move.models import Move
from application.type.models import Type
from application.pokemon.forms import PokemonForm
from application.auth.forms import AccountForm
import enum
from sqlalchemy import Integer, Enum

@app.route("/", methods=["GET"])
def index():
    account = User.query

    commonmoves = 1

    if current_user.is_authenticated:
        commonmoves = Pokemon.most_common_move_of_trainer(current_user.id)

    return render_template("index.html", pokemonlist = Pokemon.query.all(), movelist = Move.query.all(), account = account, current = current_user,
        highest_cp = Pokemon.find_highest_cp(), highest_iv = Pokemon.find_highest_iv(), commonmoves = commonmoves)

@app.route("/new_pokemon", methods=["GET"])
@login_required(role="USER")
def pokemon_form():
    fastlist = Move.allFastMoves()
    chargelist = Move.allChargedMoves()

    form = PokemonForm()

    form.fastmove.choices = [(f.id, f.name) for f in fastlist]
    form.chargemove.choices = [(c.id, c.name) for c in chargelist]

    form.firsttype.choices = [(t.value, t.name) for t in Type]
    form.secondtype.choices = [(t.value, t.name) for t in Type]

    return render_template("pokemon/new_pokemon.html", form = form)

@app.route("/new_pokemon", methods=["POST"])
@login_required(role="USER")
def pokemon_create():
    form = PokemonForm(request.form)

    fastlist = Move.allFastMoves()
    chargelist = Move.allChargedMoves()

    form.fastmove.choices = [(f.id, f.name) for f in fastlist]
    form.chargemove.choices = [(c.id, c.name) for c in chargelist]

    form.firsttype.choices = [(t.value, t.name) for t in Type]
    form.secondtype.choices = [(t.value, t.name) for t in Type]

    if not form.validate():
        return render_template("pokemon/new_pokemon.html", form = form)

    fastmove = request.form.get("fastmove")
    chargemove = request.form.get("chargemove")

    fastmove_id = fastmove[0]
    chargemove_id = chargemove[0]

    firsttypenum = request.form.get("firsttype")
    secondtypenum = request.form.get("secondtype")

    p = Pokemon(request.form.get("name"), int(request.form.get("cp")), int(request.form.get("iv")), fastmove_id, chargemove_id, firsttypenum, secondtypenum)
    p.account_id = current_user.id
    db.session().add(p)
    db.session().commit()
    return redirect(url_for("index"))

@app.route("/pokemon/<pokemon_id>", methods=["GET"])
def pokemon_view(pokemon_id):
    pokemon = Pokemon.query.get(pokemon_id)
    return render_template("pokemon/view_pokemon.html", pokemon = pokemon)

@app.route("/update_pokemon/<pokemon_id>", methods=["GET"])
@login_required(role="USER")
def pokemon_update_form(pokemon_id):
    pokemon = Pokemon.query.get(pokemon_id)

    fastlist = Move.allFastMoves()
    chargelist = Move.allChargedMoves()

    form = PokemonForm()

    form.name.data = pokemon.name
    form.cp.data = pokemon.cp
    form.iv.data = pokemon.iv

    form.fastmove.choices = [(f.id, f.name) for f in fastlist]
    form.fastmove.data = pokemon.fastmove_id
    form.chargemove.choices = [(c.id, c.name) for c in chargelist]
    form.chargemove.data = pokemon.chargemove_id

    form.firsttype.choices = [(t.value, t.name) for t in Type]
    form.firsttype.data = pokemon.first_type_id
    form.secondtype.choices = [(t.value, t.name) for t in Type]
    form.secondtype.data = pokemon.second_type_id

    return render_template("pokemon/update_pokemon.html", form = form, pokemon = pokemon)

@app.route("/update_pokemon/<pokemon_id>", methods=["POST"])
@login_required(role="USER")
def pokemon_update(pokemon_id):
    form = PokemonForm(request.form)

    fastlist = Move.allFastMoves()
    chargelist = Move.allChargedMoves()

    form.fastmove.choices = [(f.id, f.name) for f in fastlist]
    form.chargemove.choices = [(c.id, c.name) for c in chargelist]

    form.firsttype.choices = [(t.value, t.name) for t in Type]
    form.secondtype.choices = [(t.value, t.name) for t in Type]

    if not form.validate():
        return render_template("pokemon/update_pokemon.html", form = form)

    fastmove = request.form.get("fastmove")
    chargemove = request.form.get("chargemove")

    fastmove_id = fastmove[0]
    chargemove_id = chargemove[0]

    firsttypenum = request.form.get("firsttype")
    secondtypenum = request.form.get("secondtype")

    p = Pokemon.query.get(pokemon_id)
    p.name = request.form.get("name")
    p.cp = request.form.get("cp")
    p.iv = request.form.get("iv")
    p.fastmove_id = fastmove_id
    p.chargemove_id = chargemove_id
    p.first_type_id = firsttypenum
    p.second_type_id = secondtypenum

    db.session().commit()
    return redirect(url_for("index"))

@app.route("/delete_pokemon/<pokemon_id>/", methods=["POST"])
@login_required(role="USER")
def pokemon_delete(pokemon_id):
    p = Pokemon.query.get(pokemon_id)

    if p.account_id == current_user.id:
        Pokemon.query.filter_by(id=pokemon_id).delete()
        db.session().commit()
    
    return redirect(url_for("index"))
