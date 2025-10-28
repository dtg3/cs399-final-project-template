import React, { useState, useEffect } from 'react';
import { fetchTasks, updateTaskStatus, deleteTask } from '../api';
import TaskItem from '../components/TaskItem'; 
import '../App.css'; 

function TaskList() {
    const [tasks, setTasks] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const loadTasks = async () => {
        setLoading(true);
        setError(null);
        try {
            const data = await fetchTasks();
            setTasks(data);
        } catch (err) {
            setError('Could not connect to the API or fetch tasks.');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        loadTasks();
    }, []);

    // Handler passed to TaskItem for toggling status
    const handleToggleStatus = async (id, currentStatus) => {
        const newStatus = !currentStatus;
        try {
            const updatedTask = await updateTaskStatus(id, newStatus);
            
            // Update the state with the returned object
            setTasks(tasks.map(task => 
                task.id === id ? updatedTask : task
            ));
        } catch (err) {
            setError('Failed to update task status.');
            console.error(err);
        }
    };

    // Handler passed to TaskItem for deleting a task
    const handleDeleteTask = async (id) => {
        try {
            await deleteTask(id); 
            
            // Remove the task from the local state
            setTasks(tasks.filter(task => task.id !== id));
        } catch (err) {
            setError('Failed to delete task.');
            console.error(err);
        }
    };

    if (loading) return <div className="loading">Loading tasks...</div>;
    if (error) return <div className="error">Error: {error}</div>;

    return (
        <div className="task-list-page">
            <h2>Your Todo List</h2>
            
            <ul className="task-list">
                {tasks.length === 0 ? (
                    <p>No tasks yet! Go to the "Add Task" page to create one.</p>
                ) : (
                    tasks.map((task) => (
                        // Render the separate TaskItem component for each task
                        <TaskItem 
                            key={task.id}
                            task={task}
                            onToggle={handleToggleStatus}
                            onDelete={handleDeleteTask}
                        />
                    ))
                )}
            </ul>
        </div>
    );
}

export default TaskList;