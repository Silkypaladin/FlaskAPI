from flask import Blueprint
import uuid
from flask import request, jsonify
from ..extensions.security import *
from ..extensions.database import db
from ..models.users import User

user = Blueprint('user', __name__)

@user.route('/user', methods=['GET'])
def get_all_users():
    return 'All users'

@user.route('/user/<user_id>', methods=['GET'])
def get_user():
    return 'Single user with id'

@user.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_pass = hash_password(data['password'], 'sha256')
    new_user = User(str(uuid.uuid4()), data['email'], hashed_pass, data['nickname'])
    db.session.add(new_user)
    db.session.commit()
    return 'User created'

@user.route('/admin', methods=['POST'])
def create_admin():
    return 'Admin created'

@user.route('/user/<user_id>', methods=['DELETE'])
def delete_user():
    return 'User deleted'

@user.route('/admin/<admin_id>', methods=['DELETE'])
def delete_admin():
    return ''