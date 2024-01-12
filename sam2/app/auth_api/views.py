from flask import jsonify, request, make_response
from datetime import datetime, timedelta
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity, create_refresh_token, get_jwt
from werkzeug.security import check_password_hash
from ..todo.models import Todo
from ..auth.models import User
from .. import db, basic_auth
from config import Config
from . import auth_api_bp
import jwt

@basic_auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        return True
    return False

@auth_api_bp.route('/login', methods=['POST'])
def login():
    auth = request.authorization

    user = User.query.filter_by(username=auth.username).first()

    if not user or not verify_password(user.username, auth.password):
        return make_response('Invalid username or password', 401, {'WWW-Authenticate': 'Bearer realm="Authentication Required"'})
    
    access_token = create_access_token(identity=user.username, expires_delta=timedelta(minutes=30))
    refresh_token = create_refresh_token(identity=user.username)
    
    return jsonify({"access_token": access_token, "refresh_token": refresh_token})

@auth_api_bp.route('/refresh', methods=['POST'])
@jwt_required()
def refresh():
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user, expires_delta=timedelta(minutes=30))
    return jsonify({"access_token": new_token})

@auth_api_bp.route('/revoke', methods=['POST'])
@jwt_required()
def revoke():
    jti = get_jwt()['jti']
    return jsonify({"message": "Token revoked successfully"})

@auth_api_bp.route('/todos', methods=['GET'])
@jwt_required()
def get_todos():
    todos = Todo.query.all()
    todos_list = []
    for todo in todos:
        todos_list.append({
            'id': todo.id,
            'todo_item': todo.todo_item,
            'status': todo.status,
            'description': todo.description
        })
    return jsonify({'todos': todos_list})

@auth_api_bp.route('/todos', methods=['POST'])
@jwt_required()
def create_todo():
    data = request.json
    new_todo = Todo(
        todo_item=data.get('todo_item'),
        status=data.get('status', False),
        description=data.get('description')
    )
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({'message': 'Todo created successfully'}), 201

@auth_api_bp.route('/todos/<int:id>', methods=['GET'])
@jwt_required()
def get_todo(id):
    todo = Todo.query.get_or_404(id)
    return jsonify({
        'id': todo.id,
        'todo_item': todo.todo_item,
        'status': todo.status,
        'description': todo.description
    })

@auth_api_bp.route('/todos/<int:id>', methods=['PUT'])
@jwt_required()
def update_todo(id):
    todo = Todo.query.get_or_404(id)
    data = request.json
    todo.todo_item = data.get('todo_item', todo.todo_item)
    todo.status = data.get('status', todo.status)
    todo.description = data.get('description', todo.description)
    db.session.commit()
    return jsonify({'message': 'Todo updated successfully'}), 200

@auth_api_bp.route('/todos/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'message': 'Todo deleted successfully'}), 200
