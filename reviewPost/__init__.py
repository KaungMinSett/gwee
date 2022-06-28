
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviewPost.db'
app.config['SECRET_KEY'] = '2b63bf59a2cbd1f205bbe1db'
db = SQLAlchemy(app)


from reviewPost import routes