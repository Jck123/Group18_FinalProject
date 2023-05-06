from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from sqlalchemy.dialects.mysql import TINYTEXT, DATE, TEXT


class user(db.Model):
     username = db.Column(db.String(64), nullable=False)
     lname = db.Column(db.String(64), nullable=False)
     fname = db.Column(db.String(64), nullable=False)
     password = db.Column(db.String(64), nullable=False)
     id = db.Column(db.Integer, primary_key=True, autoincrement = True)
     email = db.Column(db.String(64), nullable=False)
     bio = db.Column(TINYTEXT, nullable=False)
     join_date = db.Column(DATE, nullable=False)
     
class board(db.Model):
     name = db.Column(db.String(64), nullable=False)
     description = db.Column(TINYTEXT, nullable=False)
     id = db.Column(db.Integer, primary_key=True)
     
class post(db.Model):
     contents = db.Column(TEXT(65535), nullable=False)
     id = db.Column(db.Integer, primary_key=True, autoincrement = True)
     author_id = db.Column(db.Integer, db.ForeignKey(user.id))
     board_id = db.Column(db.Integer, db.ForeignKey(board.id))
     post_date = db.Column(DATE, nullable=False)






