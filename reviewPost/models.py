
from reviewPost import db
from sqlalchemy import DateTime
from sqlalchemy.sql import func


class Post(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    postBy = db.Column(db.String(length = 30), nullable = False)
    description = db.Column(db.String(length = 1024), nullable = False, unique = True)
    tag = db.Column(db.String(length = 15), nullable = True)
    image_url = db.Column(db.String, nullable = True)
    time_created = db.Column(DateTime(timezone=True), server_default=func.now())
    time_updated = db.Column(DateTime(timezone=True), onupdate=func.now())