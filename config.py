import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class BaseConf(object):
    ORIGINS = ["*"]
    SECRET_KEY = "\xaf\x07q\xd6o\x1e/jph\xa6\xdb\xaa}\xb9\xeay\xd5\xc8\x05\xdf\xaa#\x82"
    SQLALCHEMY_DATABASE_URI = "sqlite:////" + os.path.join(BASE_DIR, "app.db")

class DevelopmentConf(BaseConf):

    PORT = 5000
    DEBUG = True
    TESTING = False
    ENV = "development"
    APPNAME = "quizDev"

class ProductionConf(BaseConf):

    PORT = 8080
    DEBUG = False
    TESTING = False
    ENV = "production"
    APPNAME = "quizProd"

    