"""root of gwee web app"""
import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

load_dotenv()
app = Flask(__name__)

user_name = os.environ.get("DATABASE_USERNAME")
password = os.environ.get("DATABASE_PASSWORD")
path = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql+psycopg2://{user_name}:{password}@{path}'
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY","")

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

#need to clarify further
from review_post import routes