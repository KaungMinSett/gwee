"""This contains all routes information for gwee"""

from flask import render_template, flash, redirect, url_for, request
from review_post import app
# from review_post import Post
from review_post.models import Admin
from review_post.forms import RegisterForm, LoginForm
from review_post import db
from flask_login import login_user


@app.route("/")
def index():
    """index page of web app"""
    return render_template("index.html")


@app.route("/home")
def home():
    """home page of web app"""
    # posts = Post.query_all()
    return render_template("home.html")


@app.route("/Login", methods= ['GET', 'POST'])
def login():
    """login page
    For GET requests, display the login form. 
    For POSTS, login the current user by processing the form. """
    # print (db)
    form = LoginForm()
    print('----------------------ssd-------------')
    print(form.validate_on_submit())
    print(form.is_submitted())
    print(form.validate())
    print("------------------sdfsdfsfs--------------")
    if form.validate_on_submit():
        attempt_admin = Admin.query.filter_by(username=form.username.data).first()
        print('-----------------kkkk--------------------')
        if attempt_admin and attempt_admin.isvalid_password(
            attempt_password = form.password.data
            ):
            print('kms')
            login_user(attempt_admin)
            flash(f'Success! you are logged in as :{attempt_admin.username}', category='success')
            return redirect(url_for('home'))
        else:
            print("ggggggggggggggg")
            flash('Username and password are not match! Please try again', category='danger')
    return render_template("login.html", form=form)
    
    
    



@app.route("/register")
def register():
    """Register page"""
    # form = RegisterForm()
    # if form.validate_on_submit():
    #     user_to_create = User(


    #     )


