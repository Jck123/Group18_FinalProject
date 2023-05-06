from models import user, post, db
from sqlalchemy import select, func
from sqlalchemy.orm import Session
import datetime
class UserRepository:
    
    def get_all_users(self):
        # TODO get all users from the DB
        all = user.query.all()
        return all
    
    def get_all_posts(self, id):
        # TODO get all posts from the DB
        return db.session.execute(select(post.contents, post.post_date, user.fname, user.lname).join(user, user.id == post.author_id).where(post.board_id==id))

    def get_user_by_name(self, name2):
        # TODO get a user from the db by username
        x = user.query.filter_by(username=name2).first()
        return x
    def get_user_by_id(self, id2):
        # TODO get a user from the db by id
        x = user.query.filter_by(id=id2).first()
        return x

    def create_user(self, fname2, lname2, username2, email2, password2):
        new_user = user(fname=fname2, lname=lname2, username=username2, email=email2, password=password2, join_date=datetime.datetime.now())
        db.session.add(new_user)
        db.session.commit()
        return new_user

    



# Singleton to be used in other modules
user_repository_singleton = UserRepository()
