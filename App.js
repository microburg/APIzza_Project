import React, { useState } from 'react';
import AdminPage from './AdminPage';
import MenuPage from './menupage';

function App() {
    // Shared state for pizzas
    const [pizzaList, setPizzaList] = useState([]); // Holds all pizzas
    const [currentPage, setCurrentPage] = useState('menu'); // Default to menu page

    return (
        <div className="App">
            {/* Navigation Bar */}
            <nav style={{ padding: '10px', background: '#FF7F32', color: 'white' }}>
                <button onClick={() => setCurrentPage('menu')} style={navButtonStyle}>
                    Menu
                </button>
                <button onClick={() => setCurrentPage('admin')} style={navButtonStyle}>
                    Admin Panel
                </button>
            </nav>

            {/* Render Current Page */}
            {currentPage === 'menu' ? (
                <MenuPage pizzaList={pizzaList} />
            ) : (
                <AdminPage pizzaList={pizzaList} setPizzaList={setPizzaList} />
            )}
        </div>
    );
}

// Navigation Button Styles
const navButtonStyle = {
    margin: '0 10px',
    padding: '10px 20px',
    color: '#fff',
    background: '#FF5C00',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer',
};

export default App;
