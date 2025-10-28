from flask import Blueprint, jsonify, request
from ..models import database as db

# This defines the blueprint and adds a prefix for the route.
tasks_bp = Blueprint('task_routes', __name__, url_prefix='/api/v1')

# Helper Function (Simplified for single-table, no User object)
def task_row_to_dict(todo_object):
    if todo_object is None: return None

    return todo_object.to_dict()


@tasks_bp.route('/todos/<int:todo_id>', methods=['PATCH'])
def update_task_status(todo_id):
    data = request.get_json()

    is_completed = data.get('completed') 

    if is_completed is None or not isinstance(is_completed, bool):
        return jsonify({'success': False, 'message': 'Boolean field "completed" is required.'}), 400

    rows_updated = db.update_task(todo_id, None, is_completed)
    
    if rows_updated == 0:
        return jsonify({'success': False, 'message': f"Todo ID {todo_id} not found."}), 404
        
    updated_todo = db.get_task_by_id(todo_id)
    return jsonify(task_row_to_dict(updated_todo)), 200


@tasks_bp.route('/todos', methods=['GET'])
def get_all_todos():

    status_filter = request.args.get('status', None)
    todos = db.get_all_tasks(status_filter)
    return jsonify(todos)


@tasks_bp.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    new_title = data.get('title') 
    
    if not new_title:
        return jsonify({'error': 'Todo title is required'}), 400

    try:
        new_todo_object = db.create_task(new_title) # DAL returns the object
    except Exception as e:
        return jsonify({'error': f"Database error: {e}"}), 500

    return jsonify(task_row_to_dict(new_todo_object)), 201


@tasks_bp.route('/todos/<int:todo_id>', methods=['GET'])
def get_single_todo(todo_id):
    
    todo_row = db.get_task_by_id(todo_id)
    
    if todo_row is None:
        return jsonify({'success': False, 'message': f"Todo ID {todo_id} not found."}), 404

    return jsonify(task_row_to_dict(todo_row))


@tasks_bp.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    rows_deleted = db.delete_task(todo_id)

    if rows_deleted == 0:
        return jsonify({'success': False, 'message': f"Todo ID {todo_id} not found."}), 404
    
    return jsonify({'success': True, 'message': f'Todo {todo_id} deleted'}), 200
