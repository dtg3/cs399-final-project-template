import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import TaskList from './pages/TaskList';
import AddTask from './pages/AddTask';
import './App.css'; 

function App() {
    return (
        <BrowserRouter>
            <div className="App">
                <h1>Simple Todo App</h1>

                {/* Navigation Links */}
                <nav>
                    <Link to="/" className="nav-link">
                        Task List
                    </Link>
                    <Link to="/add" className="nav-link">
                        Add Task
                    </Link>
                </nav>

                {/* Define Routes */}
                <Routes>
                    <Route path="/" element={<TaskList />} />
                    <Route path="/add" element={<AddTask />} />
                    <Route path="*" element={<h2>404 - Page Not Found</h2>} />
                </Routes>
            </div>
        </BrowserRouter>
    );
}

export default App;