import React from 'react';
import '../App.css'; 

function TaskItem({ task, onToggle, onDelete }) {
    // Determine the CSS class for the status button
    const statusClass = task.completed ? 'status-complete' : 'status-incomplete';

    return (
        <li className="task-item">
            <span 
                className={`task-title ${task.completed ? 'completed' : ''}`}
                onClick={() => onToggle(task.id, task.completed)}
            >
                {task.title}
            </span>
            <div>
                <button 
                    onClick={() => onToggle(task.id, task.completed)} 
                    className={`btn btn-status ${statusClass}`}
                >
                    {task.completed ? 'Completed' : 'Incomplete'}
                </button>
                <button 
                    onClick={() => onDelete(task.id)} 
                    className="btn btn-delete"
                >
                    Delete
                </button>
            </div>
        </li>
    );
}

export default TaskItem;