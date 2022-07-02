"""This contains all routes information for gwee"""

from flask import render_template
from review_post import app
# from review_post import Post
from review_post.forms import RegisterForm


@app.route("/")
def index():
    """index page of web app"""
    return render_template("index.html")


@app.route("/home")
def home():
    """home page of web app"""
    return render_template("home.html")


@app.route("/Login")
def login():
    """login page"""
    form = RegisterForm()
    return render_template("login.html", form=form)
