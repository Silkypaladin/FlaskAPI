from flask import Blueprint
import uuid
from flask import request, jsonify
from werkzeug.security import generate_password_hash
from ..extensions.database import db
from ..models import User
from .login import token_required

user = Blueprint('user', __name__)

@user.route('/api/user', methods=['GET'])
@token_required
def get_all_users(current_user):
    if not current_user.is_admin:
        return jsonify({'message' : 'Cannot perform that action!'})
        
    users = User.query.all()
    output = []

    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['email'] = user.email
        user_data['password'] = user.password
        user_data['nickname'] = user.nickname
        user_data['is_admin'] = user.is_admin
        user_data['date_created'] = user.date_created
        output.append(user_data)
    return jsonify(output)

@user.route('/api/user/<public_id>', methods=['GET'])
@token_required
def get_single_user(current_user, public_id):
    if not current_user.is_admin:
        return jsonify({'message' : 'Cannot perform that action!'})

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message' : 'No user found.'})
    user_data = {}
    user_data['public_id'] = user.public_id
    user_data['email'] = user.email
    user_data['password'] = user.password
    user_data['nickname'] = user.nickname
    user_data['is_admin'] = user.is_admin
    user_data['date_created'] = user.date_created

    return user_data

@user.route('/api/user', methods=['POST'])
@token_required
def create_user(current_user):
    if not current_user.is_admin:
       return jsonify({'message' : 'Cannot perform that action!'})

    data = request.get_json()
    hashed_pass = generate_password_hash(data['password'], method='sha256')
    new_user = User(str(uuid.uuid4()), data['email'], hashed_pass, data['nickname'])
    try:
        db.session.add(new_user)
        db.session.commit()
    except:
        return jsonify({'message' : 'User already exists!'})
    return jsonify({'message' : 'User created!'})

@user.route('/api/user/<public_id>', methods=['PUT'])
@token_required
def promote_user_account(current_user, public_id):
    if not current_user.is_admin:
        return jsonify({'message' : 'Cannot perform that action!'})

    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({'message' : 'No user found.'})
    user.is_admin = True
    db.session.commit()
    return jsonify({'message': 'Account promoted.'})
    

@user.route('/api/user/<public_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, public_id):
    if not current_user.is_admin:
        return jsonify({'message' : 'Cannot perform that action!'})
        
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({'message' : 'No user found.'})
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted.'})

