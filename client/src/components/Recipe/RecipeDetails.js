import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import './Recipe.css';

const RecipeDetails = () => {
  const { id } = useParams();
  const [recipe, setRecipe] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:5000/recipes/${id}`)
      .then(response => response.json())
      .then(data => setRecipe(data))
      .catch(error => console.error('Error fetching recipe:', error));
  }, [id]);

  if (!recipe) {
    return <div>Loading...</div>;
  }

  return (
    <div className="recipe-details">
      <img src={recipe.main_photo} alt={recipe.name} />
      <h3>{recipe.name}</h3>
      <p>{recipe.description}</p>
      <p>{recipe.ingredients}</p>
      <p>{recipe.instructions}</p>
    </div>
  );
};

export default RecipeDetails;
