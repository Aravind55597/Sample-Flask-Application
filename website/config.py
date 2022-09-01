import os
#absolute path of the directory where this file is
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = False
    #ENCRYPT SESSIONS
    SECRET_KEY = os.environ['FLASK_SECRET_KEY']
    #DATABASE URL FOR FLASK 
    #postgresql://postgres:postgres@localhost/postgres
    #Where postgres is username and postgres is password, localhost is address
    SQLALCHEMY_DATABASE_URI = os.environ['FLASK_DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS=False; 


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True