"""This contains all the features related to form"""


from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import  DataRequired
from flask_wtf.file import FileField, FileAllowed
from review_post import photos


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


class PostForm(FlaskForm):
    """Post form for admin user"""
 
    
    description = TextAreaField(label='Create another post?', validators=[DataRequired()])
    
    photo = FileField(
        validators = [
            FileAllowed(photos, 'Only images are allowed')
            ]
    )
    tag = SelectField(u'tag', choices=[('Trending'),('Promotion'),('Alert')])

    submit = SubmitField('Post')