import React, { useState } from 'react';
import './MenuPage.css';

const MenuPage = () => {
    // Sample pizza menu (hardcoded for now)
    const pizzaMenu = [
        { id: '1', name: 'Margherita', description: 'Classic with tomato and cheese', price: 5.99 },
        { id: '2', name: 'Pepperoni', description: 'Pepperoni and cheese', price: 7.99 },
        { id: '3', name: 'Veggie', description: 'Loaded with veggies', price: 6.99 },
        { id: '4', name: 'BBQ Chicken', description: 'Chicken with BBQ sauce', price: 8.99 },
    ];

    const [cart, setCart] = useState([]); // Cart state

    // Handle adding pizza to the cart
    const handleAddToCart = (pizza) => {
        setCart((prevCart) => {
            const existingItem = prevCart.find((item) => item.id === pizza.id);
            if (existingItem) {
                // Update quantity if the item already exists
                return prevCart.map((item) =>
                    item.id === pizza.id ? { ...item, quantity: item.quantity + 1 } : item
                );
            }
            // Add new item
            return [...prevCart, { ...pizza, quantity: 1 }];
        });
    };

    // Calculate total price
    const totalPrice = cart.reduce((total, item) => total + item.price * item.quantity, 0);

    return (
        <div className="menu-container">
            <h1>Pizza Menu</h1>
            <div className="menu-items">
                {pizzaMenu.map((pizza) => (
                    <div key={pizza.id} className="menu-item">
                        <h3>{pizza.name}</h3>
                        <p>{pizza.description}</p>
                        <p>Price: ${pizza.price.toFixed(2)}</p>
                        <button onClick={() => handleAddToCart(pizza)}>Add to Cart</button>
                    </div>
                ))}
            </div>

            <div className="cart-container">
                <h2>Cart</h2>
                {cart.length === 0 ? (
                    <p>Your cart is empty.</p>
                ) : (
                    <>
                        <ul>
                            {cart.map((item) => (
                                <li key={item.id}>
                                    {item.name} - ${item.price.toFixed(2)} x {item.quantity}
                                </li>
                            ))}
                        </ul>
                        <h3>Total: ${totalPrice.toFixed(2)}</h3>
                    </>
                )}
            </div>
        </div>
    );
};

export default MenuPage;
