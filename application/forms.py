from application.move.models import Move
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, validators

class PokemonForm(FlaskForm):

    name = StringField("Name", [validators.Length(min=3)])
    cp = IntegerField("CP", [validators.NumberRange(min=0, max=4500)])
    iv = IntegerField("IV", [validators.NumberRange(min=0, max=100)])
    fastmove = SelectField("Fast Move", [validators.DataRequired()], coerce=int)
    chargemove = SelectField("Charge Move", [validators.DataRequired()], coerce=int)

    #def update_choices(self, fastmoves, chargemoves):
        #self.fastmove.choices = fastmoves
        #self.chargemove.choices = chargemoves
        #fastmovechoices = []
        #for fmove in fastmoves:
        #    fastmovechoices.append((fmove.id, fmove.name))
        #self.fastmove.choices = fastmovechoices

        #chargemovechoices = []
        #for cmove in chargemoves:
        #    chargemovechoices.append((cmove.id, cmove.name))
        #self.chargemove.choices = chargemovechoices
    

    class Meta:
        csrf = False

class PokemonUpdateForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3)])
    cp = IntegerField("CP", [validators.NumberRange(min=0, max=4500)])
    iv = IntegerField("IV", [validators.NumberRange(min=0, max=100)])
    fastmove = SelectField("Fast Move", [validators.DataRequired()], coerce=int)
    chargemove = SelectField("Charge Move", [validators.DataRequired()], coerce=int)

    class Meta:
        csrf = False

class AccountForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=3)])
    password = StringField("Password", [validators.Length(min=3)])
 
    class Meta:
        csrf = False