from flask import Flask, abort, redirect, render_template, request, make_response

from models import db
from login_repository import user_repository_singleton

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'mysql://root:gKN#pvGKGN7Sth@localhost:3306/g18finalproj'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.get('/')
def index1():
    if 'userID' in request.cookies:
        return render_template('Homepage.html', log="Logout")   
    else:
        return render_template('Homepage.html', log="Login")
@app.get('/Login')
def index2():
    return render_template('login.html')
@app.get('/Logout')
def logout():
    resp = make_response(redirect('/'))
    resp.set_cookie('userID', '', expires=0)
    return resp
@app.get('/register')
def index3():
    return render_template('Registration.html')
@app.get('/user')
def index4():
     if 'userID' in request.cookies:
        name = request.cookies.get('userID')
        id = user_repository_singleton.get_user_by_id(int(name))
        return render_template('PersonalPage.html', userid=id, log="Logout")    
     else:
        return render_template('login.html', etext="Please log in to access your profile")
    
@app.get('/Login/failure')
def index5():
    return render_template('login.html', etext="Login failed, try again")
@app.get('/forum/<id>')
def index6(id):
    allposts = user_repository_singleton.get_all_posts(id)
    if 'userID' in request.cookies:
        return render_template('forum.html', posts=allposts, log="Logout")   
    else:
        return render_template('forum.html', posts=allposts, log="Login")
    



# @app.get('/users/<int:user_id>')
# def get_single_user(user_id):
#     single_user = user_repository_singleton.get_user_by_name(user_id)
#     return render_template('user.html', user=single_user)
#TODO: make user page



@app.post('/Login')
def log_in():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    if username == '' or password == '':
        abort(400)
    namecheck = user_repository_singleton.get_user_by_name(username)
    if namecheck is None:
        return redirect('/Login/failure')
    if namecheck.password == password: 
        resp = make_response(redirect('/user'))
        resp.set_cookie('userID', str(namecheck.id))
        return resp
    else:
        return redirect('/Login/failure')


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
    return redirect('/Login')

@app.post('/forum')
def create_forum():
    fname = request.form.get('firstname', '')
    lname = request.form.get('lastname', '')
    uname = request.form.get('username', '')
    pword = request.form.get('password', '')
    email = request.form.get('email', '')
    if fname == '' or lname == '' or uname == ''  or pword == ''  or email== '' :
        abort(400)
    user_repository_singleton.create_user(fname, lname, uname, email, pword)
    return redirect('/Login')