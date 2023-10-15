# handles authentication, login and so on

from flask import Blueprint, render_template, url_for, request, redirect
from werkzeug.security import generate_password_hash
from models import User
from app import db

auth = Blueprint('auth', __name__)


@auth.route('/signup')
def signup():
    return render_template('signup.html')


# below gets executed as soon as user clicks on signup
@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    #print(email, username, password)  # prints values in terminal
    user = User.query.filter_by(email=email).first()
    if user:
        print("User already already Exists!")
    new_user = User(email=email, username=username, password=generate_password_hash(password, method="pbkdf2:sha256", salt_length=16))
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))  # redirects to login page once the user is signedup


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    print(email, password)

    return redirect(url_for('main.to_do'))


@auth.route('/logout')
def logout():
    return "log out users"
