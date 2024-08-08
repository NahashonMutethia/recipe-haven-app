import React, { useState } from 'react';
import { getToken } from '../../utils';
import './Recipe.css';

function RecipeUpload() {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [ingredients, setIngredients] = useState(['']);
  const [steps, setSteps] = useState(['']);
  const [image, setImage] = useState(null);

  const handleUpload = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append('title', title);
    formData.append('description', description);
    formData.append('ingredients', JSON.stringify(ingredients));
    formData.append('steps', JSON.stringify(steps));
    if (image) formData.append('image', image);

    try {
      const response = await fetch('http://localhost:5000/recipes', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${getToken()}`,
        },
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      alert('Recipe uploaded successfully');
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleIngredientChange = (index, value) => {
    const newIngredients = [...ingredients];
    newIngredients[index] = value;
    setIngredients(newIngredients);
  };

  const handleStepChange = (index, value) => {
    const newSteps = [...steps];
    newSteps[index] = value;
    setSteps(newSteps);
  };

  const addIngredient = () => setIngredients([...ingredients, '']);

  const addStep = () => setSteps([...steps, '']);

  return (
    <div className="recipe-upload">
      <h2>Upload a Recipe</h2>
      <form onSubmit={handleUpload}>
        <input
          type="text"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
        <textarea
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          required
        ></textarea>
        <h3>Ingredients</h3>
        {ingredients.map((ingredient, index) => (
          <input
            key={index}
            type="text"
            placeholder="Ingredient"
            value={ingredient}
            onChange={(e) => handleIngredientChange(index, e.target.value)}
            required
          />
        ))}
        <button type="button" onClick={addIngredient}>Add Ingredient</button>
        <h3>Steps</h3>
        {steps.map((step, index) => (
          <textarea
            key={index}
            placeholder="Step"
            value={step}
            onChange={(e) => handleStepChange(index, e.target.value)}
            required
          ></textarea>
        ))}
        <button type="button" onClick={addStep}>Add Step</button>
        <input
          type="file"
          onChange={(e) => setImage(e.target.files[0])}
        />
        <button type="submit">Upload</button>
      </form>
    </div>
  );
}

export default RecipeUpload;
