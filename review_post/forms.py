"""This contains all the features related to form"""

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import  DataRequired


class RegisterForm(FlaskForm):
    """Register form for users"""
    username = StringField(label="Username:")
    email_address = StringField(label="Email address:")
    password = PasswordField(label="Enter Password")
    comfirm_password = PasswordField(label="Comfirm password")
    submit = SubmitField(label="Login")

class LoginForm(FlaskForm):
    """Login form for admin"""
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')