import os

class Config:
    SECRET_KEY = '323b22caac41acbf'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///temprature.db'
    # SQLALCHEMY_ECHO = f'True'
    # FLASK_DEBUG = '1'
    # FLASK_ENV = 'development'