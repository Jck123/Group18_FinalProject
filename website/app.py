from flask import Flask, abort, redirect, render_template, request

from models import db
from login_repository import user_repository_singleton

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'mysql://root:gKN#pvGKGN7Sth@localhost:3306/g18finalproj'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.get('/')
def index1():
    return redirect('/login')
# TODO: make home page
@app.get('/login')
def index2():
    return render_template('login.html')
@app.get('/register')
def index3():
    return render_template('Registration.html')
@app.get('/login/success')
def index4():
    return render_template('login.html', etext="Login successful")
@app.get('/login/failure')
def index5():
    return render_template('login.html', etext="Login failed, try again")


# @app.get('/users/<int:user_id>')
# def get_single_user(user_id):
#     single_user = user_repository_singleton.get_user_by_name(user_id)
#     return render_template('user.html', user=single_user)
#TODO: make user page



@app.post('/login')
def log_in():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    if username == '' or password == '':
        abort(400)
    namecheck = user_repository_singleton.get_user_by_name(username)
    if namecheck is None:
        return redirect('/login/failure')
    if namecheck.password == password: 
        return redirect('/login/success')
    else:
        return redirect('/login/failure')


@app.post('/register')
def create_movie():
    fname = request.form.get('firstname', '')
    lname = request.form.get('lastname', '')
    uname = request.form.get('username', '')
    pword = request.form.get('password', '')
    email = request.form.get('email', '')
    if fname == '' or lname == '' or uname == ''  or pword == ''  or email== '' :
        abort(400)
    user_repository_singleton.create_user(fname, lname, uname, email, pword)
    return redirect('/login')

