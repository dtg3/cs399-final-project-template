import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { createTask } from '../api';

function AddTask() {
    const [newTaskTitle, setNewTaskTitle] = useState('');
    const [error, setError] = useState(null);
    const navigate = useNavigate();

    const handleCreateTask = async (e) => {
        e.preventDefault();
        setError(null);
        if (!newTaskTitle.trim()) {
            setError("Task title cannot be empty.");
            return;
        }

        try {
            await createTask(newTaskTitle);
            
            setNewTaskTitle('');
            navigate('/'); 
        } catch (err) {
            setError('Failed to create task. Is the Flask server running?');
            console.error(err);
        }
    };

    return (
        <div className="add-task-page">
            <h2>Add New Task</h2>
            <form onSubmit={handleCreateTask} className="form-container">
                {error && <p className="error">{error}</p>}
                <input
                    type="text"
                    placeholder="Enter task title (e.g., Finish report)"
                    value={newTaskTitle}
                    onChange={(e) => setNewTaskTitle(e.target.value)}
                    required
                    className="form-input"
                />
                <button type="submit" className="btn btn-submit">
                    Save Task
                </button>
            </form>
        </div>
    );
}

export default AddTask;