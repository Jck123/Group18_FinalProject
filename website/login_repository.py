from models import user, db
from sqlalchemy import func
class UserRepository:
    

    def get_all_users(self):
        # TODO get all users from the DB
        all = user.query.all()
        return all

    def get_user_by_name(self, name2):
        # TODO get a user from the db by username
        x = user.query.filter_by(username=name2).first()
        return x

    def create_user(self, fname2, lname2, username2, email2, password2):
        new_user = user(fname=fname2, lname=lname2, username=username2, email=email2, password=password2)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    # def search_movies(self, title):
    #     # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
    #     x = Movie.query.filter((func.lower(Movie.title).like('%'+title.lower()+'%'))).all()
    #     return x


# Singleton to be used in other modules
user_repository_singleton = UserRepository()
