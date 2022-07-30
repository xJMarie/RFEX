from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'RFEX119'   # Encrypt/secure the cookies and session data. DO NOT SHARE THE STRING!

    from .views import views        # Call the views (blueprint)
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app