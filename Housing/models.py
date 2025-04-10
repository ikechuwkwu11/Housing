from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key= True,nullable = False)
    username = db.Column(db.String(100),unique = True, nullable = False)
    email = db.Column(db.String(200), nullable = False)
    password = db.Column(db.String(10), nullable =False)


class Housing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable = False)
    street = db.Column(db.String(100))
    number = db.Column(db.Integer)
    available = db.Column(db.Boolean,default=True)
