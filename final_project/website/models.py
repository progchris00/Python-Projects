from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User") #Understand this

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    comments = db.relationship('Comments')


#To do: review code in einstein
#Issue: can't submit new comment, make comments specific to each website.
    
