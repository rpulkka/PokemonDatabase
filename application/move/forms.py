from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, validators

class MoveForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3, max=25)])
    damage = IntegerField("Damage", [validators.NumberRange(min=1, max=300)])
    chargemove = IntegerField("Charged Move", [validators.NumberRange(min=0, max=1)])
    bars = IntegerField("Bars", [validators.NumberRange(min=0, max=10)])
    firsttype = SelectField("Type", [validators.DataRequired()], coerce=int)
 
    class Meta:
        csrf = False
