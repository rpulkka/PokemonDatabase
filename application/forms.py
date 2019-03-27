from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class PokemonForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3)])
    cp = IntegerField("CP")
    iv = IntegerField("IV")
 
    class Meta:
        csrf = False

class PokemonUpdateForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3)])
    cp = IntegerField("CP")
    iv = IntegerField("IV")

    class Meta:
        csrf = False

class AccountForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=3)])
    password = StringField("Password", [validators.Length(min=3)])
 
    class Meta:
        csrf = False