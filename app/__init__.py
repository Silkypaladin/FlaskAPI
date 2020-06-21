from flask import Flask, Blueprint
import os
from .routes.main import main
from .routes.user import user
from .extensions.database import db
from .models.users import User, Admin

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
    app.register_blueprint(main)
    app.register_blueprint(user)

    return app