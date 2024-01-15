from flask import jsonify, request, Blueprint
from sqlalchemy.exc import IntegrityError
from app.todo.models import Todo
from app import db

api_todo = Blueprint('api_todo', __name__, url_prefix='/api/todos')

@api_todo.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    todo_dict = []

    for todo in todos:
        item = {
            'id': todo.id,
            'todo_item': todo.todo_item,
            'status': todo.status,
            'description': todo.description
        }
        todo_dict.append(item)

    return jsonify(todo_dict)

@api_todo.route('/todos', methods=['POST'])
def post_todos():
    new_data = request.get_json()

    if not new_data or not all(key in new_data for key in ('todo_item', 'status', 'description')):
        return jsonify({"message": "Invalid data or missing keys"}), 400

    todo = Todo(todo_item=new_data['todo_item'], status=new_data['status'], description=new_data['description'])

    db.session.add(todo)
    db.session.commit()

    return jsonify({
        "id": todo.id,
        "todo_item": todo.todo_item,
        "status": todo.status,
        "description": todo.description
    }), 201

@api_todo.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    todo = Todo.query.get_or_404(id)

    return jsonify({
        "id": todo.id,
        "todo_item": todo.todo_item,
        "status": todo.status,
        "description": todo.description
    })

@api_todo.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = Todo.query.get_or_404(id)
    data = request.get_json()

    if not data:
        return jsonify({"message": "No input data provided"}), 400

    todo.todo_item = data.get('todo_item', todo.todo_item)
    todo.status = data.get('status', todo.status)
    todo.description = data.get('description', todo.description)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()

    return jsonify({"message": "Todo was updated"}), 204

@api_todo.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"message": "Resource successfully deleted."}), 200
