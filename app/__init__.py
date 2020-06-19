from flask import Flask, Blueprint
import os
from .views.main import main
from .extensions.database import db

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)

    app.register_blueprint(main)

    return app