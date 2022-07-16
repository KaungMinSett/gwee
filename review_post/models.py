"""This contains model of the web app gwee"""

import bcrypt
from sqlalchemy import DateTime, true
from sqlalchemy.sql import func
from flask_login import UserMixin

from review_post import db, bcrypt, login_manager

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))


class Admin(db.Model, UserMixin):
    """Admin table"""
    # pylint: disable=no-member,too-few-public-methods
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    # email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=500), nullable=False)
    # authenticated = db.Column(db.Boolean, default=False)
    posts = db.relationship("Post", backref="posted_by", lazy=True)

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_password):
        self.password_hash = bcrypt.generate_password_hash(plain_password).decode('utf-8')
    

    def isvalid_password(self, attempt_password):
        
        return bcrypt.check_password_hash(self.password_hash, attempt_password)
           


class Post(db.Model):
    """post table"""
    # pylint: disable=no-member,too-few-public-methods
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    tag = db.Column(db.String(length=15), nullable=True)
    image_url = db.Column(db.String, nullable=True)
    owner = db.Column(db.String, db.ForeignKey("admin.username"))
    time_created = db.Column(DateTime(timezone=True), server_default=func.now())
    time_updated = db.Column(DateTime(timezone=True), onupdate=func.now())
