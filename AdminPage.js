import React, { useState } from 'react';
import Message from './Message';
import './AdminPage.css';

const AdminPage = () => {
    const [pizzaID, setPizzaID] = useState(''); // State for Pizza ID input
    const [pizzaName, setPizzaName] = useState('');
    const [pizzaDescription, setPizzaDescription] = useState('');
    const [pizzaPrice, setPizzaPrice] = useState('');
    const [updatePizzaID, setUpdatePizzaID] = useState('');
    const [newPizzaPrice, setNewPizzaPrice] = useState('');
    const [message, setMessage] = useState(null);

    const [pizzaList, setPizzaList] = useState([]); // State to manage pizzas

    // Handle Adding a New Pizza
    const handleAddPizzaSubmit = (e) => {
        e.preventDefault();

        // Check for duplicate IDs
        const idExists = pizzaList.some((pizza) => pizza.id === pizzaID.trim());
        if (idExists) {
            setMessage({ text: 'Pizza ID already exists. Please use a unique ID.', type: 'error' });
            return;
        }

        // Add the new pizza to the pizza list
        const newPizza = {
            id: pizzaID.trim(), // Use the mandatory Pizza ID
            name: pizzaName,
            description: pizzaDescription,
            price: parseFloat(pizzaPrice),
        };

        setPizzaList([...pizzaList, newPizza]); // Update the pizza list
        setMessage({ text: 'Pizza added successfully!', type: 'success' });

        // Reset form
        setPizzaID('');
        setPizzaName('');
        setPizzaDescription('');
        setPizzaPrice('');
    };

    // Handle Updating Pizza Price by ID
    const handleUpdatePriceSubmit = (e) => {
        e.preventDefault();

        const updatedList = pizzaList.map((pizza) =>
            pizza.id.toString() === updatePizzaID
                ? { ...pizza, price: parseFloat(newPizzaPrice) }
                : pizza
        );

        const pizzaFound = pizzaList.some((pizza) => pizza.id.toString() === updatePizzaID);

        if (pizzaFound) {
            setPizzaList(updatedList);
            setMessage({ text: 'Pizza price updated successfully!', type: 'success' });
        } else {
            setMessage({ text: 'Pizza ID not found!', type: 'error' });
        }

        // Reset form
        setUpdatePizzaID('');
        setNewPizzaPrice('');
    };

    return (
        <div className="container">
            <h1>Pizza Admin Panel</h1>

            {/* Add Pizza Form */}
            <div className="form-container">
                <h2>Add a New Pizza</h2>
                <form onSubmit={handleAddPizzaSubmit}>
                    <label>Pizza ID:</label>
                    <input
                        type="text"
                        value={pizzaID}
                        onChange={(e) => setPizzaID(e.target.value)}
                        required
                        placeholder="Enter a unique ID for the pizza"
                    />

                    <label>Pizza Name:</label>
                    <input
                        type="text"
                        value={pizzaName}
                        onChange={(e) => setPizzaName(e.target.value)}
                        required
                    />

                    <label>Description:</label>
                    <textarea
                        value={pizzaDescription}
                        onChange={(e) => setPizzaDescription(e.target.value)}
                        required
                    ></textarea>

                    <label>Price:</label>
                    <input
                        type="number"
                        value={pizzaPrice}
                        onChange={(e) => setPizzaPrice(e.target.value)}
                        min="0"
                        step="0.01"
                        required
                    />

                    <button type="submit">Add Pizza</button>
                </form>
            </div>

            {/* Update Pizza Price Form */}
            <div className="form-container">
                <h2>Update Pizza Price</h2>
                <form onSubmit={handleUpdatePriceSubmit}>
                    <label>Pizza ID:</label>
                    <input
                        type="text"
                        value={updatePizzaID}
                        onChange={(e) => setUpdatePizzaID(e.target.value)}
                        required
                    />

                    <label>New Price:</label>
                    <input
                        type="number"
                        value={newPizzaPrice}
                        onChange={(e) => setNewPizzaPrice(e.target.value)}
                        min="0"
                        step="0.01"
                        required
                    />

                    <button type="submit">Update Price</button>
                </form>
            </div>

            {/* Pizza List */}
            <div className="pizza-list">
                <h2>Pizza List</h2>
                {pizzaList.length === 0 ? (
                    <p>No pizzas added yet.</p>
                ) : (
                    <table>
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Name</th>
                                <th>Description</th>
                                <th>Price ($)</th>
                            </tr>
                        </thead>
                        <tbody>
                            {pizzaList.map((pizza) => (
                                <tr key={pizza.id}>
                                    <td>{pizza.id}</td>
                                    <td>{pizza.name}</td>
                                    <td>{pizza.description}</td>
                                    <td>{pizza.price.toFixed(2)}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                )}
            </div>

            {/* Message Component */}
            {message && <Message text={message.text} type={message.type} />}
        </div>
    );
};

export default AdminPage;
