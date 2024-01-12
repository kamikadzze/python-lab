import os
from os import path, environ
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

ACCESS_EXPIRES = {
    'access': timedelta(minutes=1),
    'refresh': timedelta(days=1)
}
class Config:
    DEBUG = False
    DEVELOPMENT = False
    SECRET_KEY = environ.get('SECRET_KEY') or \
        'mysecretkey'
    FLASK_SECRET = SECRET_KEY
    JWT_SECRET_KEY = "super-secret" 
    JWT_ACCESS_TOKEN_EXPIRES = ACCESS_EXPIRES['access']
    JWT_REFRESH_TOKEN_EXPIRES = ACCESS_EXPIRES['refresh']
    


class LocalConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app/site.sqlite')

class TestConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app/test_db.sqlite')
    WTF_CSRF_ENABLED = False

    
config = {
    'local': LocalConfig,
    'test': TestConfig
}