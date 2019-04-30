from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class AccountForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=3, max=25)])
    password = StringField("Password", [validators.Length(min=3, max=25)])
 
    class Meta:
        csrf = False
  
class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=3, max=20)])
    password = PasswordField("Password", [validators.Length(min=3, max=20)])
  
    class Meta:
        csrf = False
