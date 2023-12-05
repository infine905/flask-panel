from flask import Flask, render_template, redirect, url_for, flash, get_flashed_messages, request
from flask import session as Session
from flask_bootstrap import Bootstrap

from functools import wraps
from datetime import timedelta

from app.config import CONFIG
from app.UserController import UserController

app = Flask(__name__)
Bootstrap(app)
app.secret_key = CONFIG['secret_key']
app.permanent_session_lifetime = timedelta(hours=1)

User = UserController()

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in Session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect('/login')
    return wrap

def no_login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in Session:
            return redirect('/')
        else:
            return f(*args, **kwargs)
    return wrap

def ban_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in Session and 'username' in Session:
            if User.isBanned(Session['username']):
                return f(*args, **kwargs)
        return redirect('/')
    return wrap

def ban_check(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in Session and 'username' in Session:
            if User.isBanned(Session['username']):
                return redirect('/banned')
        return f(*args, **kwargs)
    return wrap  

def get_last_error() -> str:
    errors = get_flashed_messages()
    if len(errors) > 0:
        return str(errors[-1])
    else:
        return ''
    
@app.route('/', methods=['GET', 'POST'])
@ban_check
def index_page():
    isAdmin = False
    isBanned = False
    if 'logged_in' in Session and 'username' in Session:
        isAdmin = User.isAdmin(Session['username'])
        isBanned = User.isBanned(Session['username'])
    return render_template('home.html', site_name=CONFIG['site_name'], session=Session, isAdmin=isAdmin, isBanned=isBanned)

@app.route('/login', methods=['GET', 'POST'])
@no_login_required
def login_page():   
    error = get_last_error()      
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if User.userLogin(username, password) == True:
            Session['logged_in'] = True 
            Session['username'] = username
            return redirect('/')
        else:
            error = 'Invalid username or password'
            flash(error)
    return render_template('login.html', site_name=CONFIG['site_name'], error=error)

@app.route('/register', methods=['GET', 'POST'])
@no_login_required
def register_page():   
    error = get_last_error()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        try:
            if User.userRegister(username, password, confirm_password) == True:
                    Session['logged_in'] = True
                    Session['username'] = username 
                    return redirect('/')
        except Exception as e:
            error = str(e)
            flash(error)
    return render_template('register.html', site_name=CONFIG['site_name'], error=error)

@app.route('/logout')
@login_required
def logout():
    Session.pop('logged_in', None)
    Session.pop('username', None)
    return redirect('/login')

@app.route('/banned', methods=['GET', 'POST'])
@ban_required
def banned_page():
    username = Session['username']
    ban_reason = User.getBanReason(username)
    return render_template('banned.html', site_name = CONFIG['site_name'], ban_reason=ban_reason)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=False)