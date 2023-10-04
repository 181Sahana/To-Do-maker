#This is the first file to run in any flask application
from flask import Flask 

#acts as main() function, when a flask is run, it looks for create_app 
def create_app():
    app = Flask(__name__)

    #communicating with main.py
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #communicating with auth.py
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)


    return app



