
from reviewPost import app
from flask import render_template
# from reviewPost import Post
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/adminLogin")
def login():
    return render_template("login.html")