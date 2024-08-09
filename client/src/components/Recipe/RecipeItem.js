import React from 'react';
import './Recipe.css';

const RecipeItem = ({ recipe }) => {
    return (
        <div className="recipe-item">
            <img src={recipe.main_photo} alt={recipe.name} />
            <h3>{recipe.name}</h3>
            <p>{recipe.description}</p>
        </div>
    );
};

export default RecipeItem;
