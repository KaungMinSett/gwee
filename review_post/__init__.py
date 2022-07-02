"""root of gwee web app"""
import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///reviewPost.db"
app.config["SECRET_KEY"] = os.environ.get("GWEE_DATABASE_KEY","")

db = SQLAlchemy(app)
