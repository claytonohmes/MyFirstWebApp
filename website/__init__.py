from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    '''
    the purpose of this function is to build a flask app. This function returns the app object.
    '''
    app = Flask(__name__)
    #this is to secure browser data. just needs to be a random string.
    app.config['SECRET_KEY'] = 'fasdfaiuthndsjfhgnmnwehrwqejpoiuda'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    #anything defined as prefix here will be the route BEFORE you can get to the views within auth or views
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from . import models

    with app.app_context():
        db.create_all()

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')