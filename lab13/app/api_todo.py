from flask import Blueprint, jsonify, request
from .models import Todo
from . import db 

api_todo_bp = Blueprint('api', __name__, url_prefix='/api')

@api_todo_bp.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    todo_list = [{'id': todo.id, 'todo_item': todo.todo_item, 'status': todo.status, 'description': todo.description} for todo in todos]
    return jsonify({'todos': todo_list})

@api_todo_bp.route('/todos', methods=['POST'])
def create_todo():
    data = request.json
    new_todo = Todo(todo_item=data.get('todo_item'), status=data.get('status'), description=data.get('description'))
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({'message': 'Todo created successfully'})

@api_todo_bp.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    todo = Todo.query.get_or_404(id)
    todo_data = {'id': todo.id, 'todo_item': todo.todo_item, 'status': todo.status, 'description': todo.description}
    return jsonify(todo_data)

@api_todo_bp.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = Todo.query.get_or_404(id)
    data = request.json
    todo.todo_item = data.get('todo_item', todo.todo_item)
    todo.status = data.get('status', todo.status)
    todo.description = data.get('description', todo.description)
    db.session.commit()
    return jsonify({'message': 'Todo updated successfully'})

@api_todo_bp.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'message': 'Todo deleted successfully'})
