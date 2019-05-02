from application.move.models import Move
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, validators

class PokemonForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3, max=15)])
    cp = IntegerField("CP", [validators.NumberRange(min=10, max=4500)])
    iv = IntegerField("IV", [validators.NumberRange(min=0, max=100)])
    fastmove = SelectField("Fast Move", [validators.DataRequired()], coerce=int)
    chargemove = SelectField("Charge Move", [validators.DataRequired()], coerce=int)
    firsttype = SelectField("First Type", [validators.DataRequired()], coerce=int)
    secondtype = SelectField("Second Type", [validators.DataRequired()], coerce=int)

    def validate(self):
        if not FlaskForm.validate(self):
            return False
        result = True
        seen = set()
        for field in [self.firsttype, self.secondtype]:
            if field.data in seen:
                field.errors.append('The two types should be different.')
                result = False
            else:
                seen.add(field.data)
        return result

    class Meta:
        csrf = False
