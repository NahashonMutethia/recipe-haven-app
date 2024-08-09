import React from 'react';
import { Link } from 'react-router-dom';
import './Recipe.css';

function RecipeItem({ recipe }) {
  return (
    <div className="recipe-item">
      <h3>{recipe.title}</h3>
      <p>{recipe.description}</p>
      <Link to={`/recipes/recipes/${recipe.id}`}>View Details</Link>
    </div>
  );
}

export default RecipeItem;
