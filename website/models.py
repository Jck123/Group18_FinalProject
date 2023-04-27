from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from sqlalchemy.dialects.mysql import TINYTEXT


class user(db.Model):
     username = db.Column(db.String(64), nullable=False)
     lname = db.Column(db.String(64), nullable=False)
     fname = db.Column(db.String(64), nullable=False)
     password = db.Column(db.String(64), nullable=False)
     id = db.Column(db.Integer, primary_key=True, autoincrement = True)
     email = db.Column(db.String(64), nullable=False)
     bio = db.Column(TINYTEXT, nullable=False)



