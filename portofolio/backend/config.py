import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

def run():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/portofolio'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portofolio.db'
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from users.routes import user
    from about.routes import about
    from api.routes import api
    #from errors.handlers import errors

    # app.register_blueprint(users)
    # app.register_blueprint(posts)
    app.register_blueprint(user)
    app.register_blueprint(api)
    # app.register_blueprint(errors)

    return app
