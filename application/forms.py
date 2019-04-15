from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class PokemonForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3)])
    cp = IntegerField("CP", [validators.NumberRange(min=0, max=4500)])
    iv = IntegerField("IV", [validators.NumberRange(min=0, max=100)])
    fastMove_id = IntegerField("Fast Move ID")
    chargeMove_id = IntegerField("Charge Move ID")
 
    class Meta:
        csrf = False

class PokemonUpdateForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3)])
    cp = IntegerField("CP", [validators.NumberRange(min=10, max=4500)])
    iv = IntegerField("IV", [validators.NumberRange(min=0, max=100)])
    fastMove_id = IntegerField("Fast Move ID")
    chargeMove_id = IntegerField("Charge Move ID")

    class Meta:
        csrf = False

class AccountForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=3)])
    password = StringField("Password", [validators.Length(min=3)])
 
    class Meta:
        csrf = False