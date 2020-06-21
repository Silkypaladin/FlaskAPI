from flask import Blueprint
import uuid
from flask import request, jsonify
from ..extensions.security import *
from ..extensions.database import db
from ..models.users import User, Admin

user = Blueprint('user', __name__)

@user.route('/user', methods=['GET'])
def get_all_users():
    users = User.query.all()
    output = []

    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['email'] = user.email
        user_data['password'] = user.password
        user_data['nickname'] = user.nickname
        user_data['active'] = user.active
        user_data['date_created'] = user.date_created
        output.append(user_data)
    return jsonify(output)

@user.route('/user/<public_id>', methods=['GET'])
def get_user(public_id):
    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message' : 'No user found.'})
    user_data = {}
    user_data['public_id'] = user.public_id
    user_data['email'] = user.email
    user_data['password'] = user.password
    user_data['nickname'] = user.nickname
    user_data['active'] = user.active
    user_data['date_created'] = user.date_created

    return user_data

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
    data = request.get_json()
    hashed_pass = hash_password(data['password'], 'sha256')
    new_admin = Admin(str(uuid.uuid4()), hashed_pass, data['nickname'])
    db.session.add(new_admin)
    db.session.commit()
    return 'Admin created'

@user.route('/user/<public_id>', methods=['DELETE'])
def delete_user(public_id):
    return 'User deleted'

@user.route('/admin/<public_id>', methods=['DELETE'])
def delete_admin(public_id):
    return ''