from flask_login import UserMixin # provides default implementations of properties and methods for user management in flask
from __init__ import db # imports database information from init

# creates code template for creating objects about User
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # Creates id column on table with a primary key constraint which uniquely identifies each record in a SQLAlchemy table
    email = db.Column(db.String(100), unique=True) # Creates email column with a unique property saying that each email has to be different
    password = db.Column(db.String(100)) # Creates password column storing the user's password
    name = db.Column(db.String(1000)) # Creates name column, storing the user's name