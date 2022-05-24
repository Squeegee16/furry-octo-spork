from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from os import path
from website.config import Config
# from website.datalogger2 import log
import threading

db = SQLAlchemy()

def temp(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    # from website.errors.handlers import errors
    from website.main.main import main

    # app.register_blueprint(errors)
    app.register_blueprint(main)#, url_prefix='/')

    from website.models import Temprature

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + 'temprature.db'):
        db.create_all(app=app)
        print('Created Database!')
    else:
        print('using existing Database')
