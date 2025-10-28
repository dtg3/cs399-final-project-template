# tests/test_routes.py
import json
import pytest
from app.models.database import Todo 


def test_update_todo_status(client, db_conn):
    incomplete_task = db_conn.query(Todo).filter_by(completed=False).first()
    task_id = incomplete_task.id
    
    response = client.patch(
        f'/api/v1/todos/{task_id}', 
        data=json.dumps({'completed': True}),
        content_type='application/json'
    )
    
    assert response.status_code == 200
    assert response.json['completed'] == True
    
    updated_task = db_conn.get(Todo, task_id) 
    assert updated_task.completed == True


def test_delete_todo(client, db_conn):
    task_to_delete = Todo(title='task_to_delete')
    db_conn.add(task_to_delete)
    db_conn.commit() 
    task_id = task_to_delete.id 

    response = client.delete(f'/api/v1/todos/{task_id}')
    assert response.status_code == 200
    
    task_row = db_conn.get(Todo, task_id)
    
    assert task_row is None