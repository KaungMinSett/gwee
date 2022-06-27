
from reviewPost import db
from sqlalchemy import DateTime
from sqlalchemy.sql import func


class User(db.Model):
     id = db.Column(db.Integer, primary_key = True)
     username = db.Column(db.String(length = 30), nullable = False, unique = True)
     email_address = db.Column(db.String(length = 50), nullable = False, unique = True)
     password_hash = db.Column(db.String(length = 60), nullable = False)
     posts = db.relationship('Post', backref='posted_by', lazy = True)





class Post(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(length = 1024), nullable = False, unique = True)
    tag = db.Column(db.String(length = 15), nullable = True)
    image_url = db.Column(db.String, nullable = True)
    owner = db.Column(db.String, db.ForeignKey('user.username'))
    time_created = db.Column(DateTime(timezone=True), server_default=func.now())
    time_updated = db.Column(DateTime(timezone=True), onupdate=func.now())

