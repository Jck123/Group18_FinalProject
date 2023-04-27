from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from sqlalchemy.dialects.mysql import TINYTEXT
# class Instructor(db.Model):
#     instructor_id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(255), nullable=False)
#     last_name = db.Column(db.String(255), nullable=False)
#     tenured = db.Column(db.Boolean, nullable=False)
# -- Create movie table
# CREATE TABLE movie (
#     movie_id SERIAL       NOT NULL,
#     title    VARCHAR(255) NOT NULL,
#     director VARCHAR(255) NOT NULL,
#     rating   INT NOT      NULL,
#     PRIMARY KEY (movie_id)
# );

class user(db.Model):
     username = db.Column(db.String(64), nullable=False)
     lname = db.Column(db.String(64), nullable=False)
     fname = db.Column(db.String(64), nullable=False)
     password = db.Column(db.String(64), nullable=False)
     id = db.Column(db.Integer, primary_key=True, autoincrement = True)
     email = db.Column(db.String(64), nullable=False)
     bio = db.Column(TINYTEXT, nullable=False)



