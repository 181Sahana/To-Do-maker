#handles CRUD operatins

from flask import Blueprint, render_template, url_for

#initializing main file
#Blueprint is way to organize the files inside a flask application 
#setting up blueprint for the flask application
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('home.html')

@main.route('/profile')
def profile():
    return 'Profile Here!'