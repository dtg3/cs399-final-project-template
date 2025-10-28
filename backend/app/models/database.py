# This will handle setting up and defining my Models
#   which translates to tables in the database as well
#   as provide functions to help interact with the data
#   from the routes.

from datetime import datetime, timezone
from .. import db # This is our SQLAlchemy object from __init__.py

# This is our data model representing the todo table.
class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False) 
    completed = db.Column(db.Boolean, default=False, nullable=False)


    # Handy function to convert the class data into a Python dictionary
    #   which makes API JSON responses easier to create.
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'created_at': self.created_at.isoformat(),
            'completed': self.completed
        }


# These are a series of functions that form the Data Access Layer (DAL)
#   These functions are simple interactions between your routes and
#   SQLAlchemy.

def create_task(title, completed=False):
    new_todo = Todo(title=title, completed=completed)
    db.session.add(new_todo)
    db.session.commit()
    return new_todo


def get_all_tasks(status_filter=None):
    query = db.session.query(Todo).order_by(Todo.created_at.asc())
    
    if status_filter == 'completed':
        query = query.filter(Todo.completed == True)
    elif status_filter == 'incomplete':
        query = query.filter(Todo.completed == False)
    
    # Returns a list of dictionaries, as defined in Todo.to_dict()
    return [task.to_dict() for task in query.all()]


def get_task_by_id(task_id):
    return db.session.get(Todo, task_id)


# Function that uses the modern SQLAlchemy 2.0 API (Fix for LegacyAPIWarning)
def update_task(task_id, title=None, completed=None):
    todo = db.session.get(Todo, task_id)
    
    if todo:
        if title is not None:
            todo.title = title
        if completed is not None:
            todo.completed = completed
        
        db.session.commit()
    
    return todo
    

def delete_task(task_id):
    todo = db.session.get(Todo, task_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return True
    return False


def list_tasks(status_filter=None):
    query = db.session.query(Todo).order_by(Todo.created_at.asc())
    
    if status_filter == 'completed':
        query = query.filter(Todo.completed == True)
    elif status_filter == 'incomplete':
        query = query.filter(Todo.completed == False)
        
    return [task.to_dict() for task in query.all()]
