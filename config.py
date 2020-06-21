import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class BaseConf(object):
    ORIGINS = ["*"]
    SECRET_KEY = "\xa88*k$9^,\x910\x87\x1e@\x1eb\t\xcd\x1b\xa3\xdb\xd7(2\xf6"
    SQLALCHEMY_DATABASE_URI = "sqlite:////" + os.path.join(BASE_DIR, "app.db")

class DevelopmentConf(BaseConf):

    PORT = 5000
    DEBUG = True
    TESTING = False
    ENV = 'development'
    APPNAME = "quizDev"

class ProductionConf(BaseConf):

    PORT = 8080
    DEBUG = False
    TESTING = False
    ENV = 'production'
    APPNAME = "quizProd"

    