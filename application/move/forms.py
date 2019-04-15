from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, validators

class MoveForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3)])
    damage = IntegerField("Damage", [validators.NumberRange(min=0, max=300)])
    chargeMove = BooleanField("Charged Move")
    bars = IntegerField("Bars", [validators.NumberRange(min=0, max=10)])
 
    class Meta:
        csrf = False

class MoveUpdateForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3)])
    damage = IntegerField("Damage", [validators.NumberRange(min=0, max=300)])
    chargeMove = BooleanField("Charged Move")
    bars = IntegerField("Bars", [validators.NumberRange(min=0, max=10)])
 
    class Meta:
        csrf = False