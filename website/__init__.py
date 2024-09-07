from flask import Flask


def create_app():
    '''
    the purpose of this function is to build a flask app. This function returns the app object.
    '''
    app = Flask(__name__)
    #this is to secure browser data. just needs to be a random string.
    app.config['SECRET_KEY'] = 'fasdfaiuthndsjfhgnmnwehrwqejpoiuda'

    from .views import views
    from .auth import auth

    #anything defined as prefix here will be the route BEFORE you can get to the views within auth or views
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

