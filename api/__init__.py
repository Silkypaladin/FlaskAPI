from flask import Flask, Blueprint
import os
from .routes.user import user
from .routes.login import login
from .extensions.database import db
from .models import User

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
    app.register_blueprint(user)
    app.register_blueprint(login)

    return app