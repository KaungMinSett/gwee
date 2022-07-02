"""This contains all the features related to form"""

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField


class RegisterForm(FlaskForm):
    """Register form for users"""
    username = StringField(label="Username:")
    email_address = StringField(label="Email address:")
    password = PasswordField(label="Create Password")
    comfirm_password = PasswordField(label="Comfirm password")
    submit = SubmitField(label="Create Account")
