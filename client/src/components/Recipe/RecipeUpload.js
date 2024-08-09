import React, { useState } from 'react';
import './Recipe.css';

const RecipeUpload = () => {
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    ingredients: '',
    instructions: '',
    main_photo: '',
  });

  const handleChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = e => {
    e.preventDefault();
    const token = localStorage.getItem('token'); // Assuming the JWT is stored in localStorage

    fetch('http://127.0.0.1:5000/recipes', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
      },
      body: JSON.stringify(formData),
    })
      .then(response => response.json())
      .then(data => {
        console.log('Recipe added:', data);
      })
      .catch(error => console.error('Error adding recipe:', error));
  };

  return (
    <div className="recipe-upload">
      <h2>Upload New Recipe</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="Recipe Name"
          value={formData.name}
          onChange={handleChange}
        />
        <textarea
          name="description"
          placeholder="Recipe Description"
          value={formData.description}
          onChange={handleChange}
        />
        <textarea
          name="ingredients"
          placeholder="Ingredients"
          value={formData.ingredients}
          onChange={handleChange}
        />
        <textarea
          name="instructions"
          placeholder="Instructions"
          value={formData.instructions}
          onChange={handleChange}
        />
        <input
          type="text"
          name="main_photo"
          placeholder="Main Photo URL"
          value={formData.main_photo}
          onChange={handleChange}
        />
        <button type="submit">Add Recipe</button>
      </form>
    </div>
  );
};

export default RecipeUpload;
