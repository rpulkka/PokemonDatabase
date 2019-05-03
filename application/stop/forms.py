from flask_wtf import FlaskForm
from wtforms import StringField, validators

class StopForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3, max=25)])
    city = StringField("City", [validators.Length(min=3, max=25)])

    class Meta:
        csrf = False