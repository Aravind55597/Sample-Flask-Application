from zipapp import create_archive
from flask import Flask; 
from flask_sqlalchemy import SQLAlchemy;
from os import path ; 
#importing stuff form current directory .<filename>
from .config import Config; 

#manages login for your app
from flask_login import LoginManager

#variables defined here can be retrieved as "from . import db" 
db=SQLAlchemy(); 

#__init__ files tells python to treat directories as modules 
#hold the names of all the methods in all the Python files that are in its immediate directory
def create_app(): 
    #module name "website" is passed to flask
    app=Flask(__name__); 

    #load configuration from config.py 
    app.config.from_object(Config()); 

    #initialise database
    db.init_app(app); 

    #register your blueprints 
    from .views import views
    from .auth import auth 

    app.register_blueprint(views,url_prefix='/'); 
    app.register_blueprint(auth,url_prefix='/'); 

    #import models so as to register them
    #you can also import the models individually
    from  . import models

    create_database(app); 

    #Flask-Login provides user session management for Flask. It handles the common tasks of logging in, 
    #logging out, and remembering your users’ sessions over extended periods of time.
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # This callback is used to reload the user object from the user ID stored in the session.
    # user_id will come from the user session. If they're logged in, 
    # they will have it set as their identity. When a request comes in, 
    # user loader attempts to load a user object using this identity and 
    # check whether the user exists and is active (not blocked). 
    # If all goes well the user is considered authenticated and 
    # the object user loader returns can be accessed across the app (within request context) as current_user
    @login_manager.user_loader
    def load_user(id):
        return models.User.query.get(int(id))

    return app; 

def create_database(app): 
    db.create_all(app=app); 