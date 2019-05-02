from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField, validators, ValidationError

class MoveForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3, max=25)])
    damage = IntegerField("Damage", [validators.NumberRange(min=1, max=300)])
    chargemove = BooleanField("Charged Move")
    bars = IntegerField("Bars", [validators.NumberRange(min=0, max=10)])
    firsttype = SelectField("Type", [validators.DataRequired()], coerce=int)

#    def validate(self):
#        if not FlaskForm.validate(self):
#            return False
#        result = True
#
#        if self.chargemove == 1 and self.bars == 0:
#            raise ValidationError('Charge moves must have 1-8 bars.') 
#            result = False
#
#        if self.chargemove == 0 and self.bars != 0:
#            self.bars = 0
#        
#        return result
 
    class Meta:
        csrf = False

