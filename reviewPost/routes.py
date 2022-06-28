
from reviewPost import app
from flask import render_template
# from reviewPost import Post
from reviewPost.forms import RegisterForm
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/Login")
def login():
    form = RegisterForm()
    return render_template("login.html", form = form)
