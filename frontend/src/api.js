import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:5000/api/v1';

// Create an instance of Axios for cleaner base URL usage
const api = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

export const fetchTasks = async (statusFilter = null) => {
    try {
        const response = await api.get('/todos', {
            params: statusFilter ? { status: statusFilter } : {},
        });
        return response.data;
    } catch (error) {
        console.error('API Error in fetchTasks:', error);
        throw new Error('Failed to fetch tasks from the server.');
    }
};

export const createTask = async (title) => {
    try {
        const response = await api.post('/todos', { title });
        return response.data;
    } catch (error) {
        console.error('API Error in createTask:', error);
        throw new Error('Failed to create task.');
    }
};

export const updateTaskStatus = async (id, completed) => {
    try {
        const response = await api.patch(`/todos/${id}`, { completed }); 
        return response.data; 
    } catch (error) {
        console.error('API Error in updateTaskStatus:', error);
        throw new Error('Failed to update task status.');
    }
};

export const deleteTask = async (id) => {
    try {
        const response = await api.delete(`/todos/${id}`);
        return response.data;
    } catch (error) {
        console.error('API Error in deleteTask:', error);
        throw new Error('Failed to delete task.');
    }
};
