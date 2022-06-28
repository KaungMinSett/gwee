from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label = 'Username:')
    email_address = StringField(label = 'Email address:')
    password = PasswordField(label = 'Create Password')
    comfirm_password = PasswordField (label = 'Comfirm password')
    submit = SubmitField (label = "Create Account")
