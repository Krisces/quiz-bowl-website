from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

#Define a new database
db=SQLAlchemy()
DB_NAME="database.db"

#Function to create the app and appoint it with a database
def create_app():
    app=Flask(__name__)                                                           
    app.config['SECRET_KEY']='krossekrabbepizzaistdiepizzanurfuerdichundmich'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'   #Define database location
    db.init_app(app)

    #Import blueprints
    from .views import views
    from .auth import auth


    #Register blueprints with flask
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    create_database(app)

    login_manager=LoginManager()
    login_manager.login_view='auth.login'        #where to redirect if not logged in
    login_manager.init_app(app)                  #telling login manager which app is used

    #Telling flask how to load the user and what user I'm looking for 
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

#Create the actual database and implement models
def create_database(app):
    db_path = path.join('website', DB_NAME)
    if not path.exists(db_path):
        db.create_all(app=app)
        print('Created Database!')
