import React, { useState } from 'react';
import './Recipe.css';

const Search = () => {
  const [query, setQuery] = useState('');
  const [filterBy, setFilterBy] = useState('name');
  const [results, setResults] = useState([]);

  const handleSearch = e => {
    e.preventDefault();

    fetch(`http://127.0.0.1:5000/recipes/recipes/search?query=${query}&filter_by=${filterBy}`)
      .then(response => response.json())
      .then(data => setResults(data))
      .catch(error => console.error('Error searching recipes:', error));
  };

  return (
    <div className="recipe-search">
      <input
        type="text"
        placeholder="Search recipes..."
        value={query}
        onChange={e => setQuery(e.target.value)}
      />
      <select value={filterBy} onChange={e => setFilterBy(e.target.value)}>
        <option value="name">Name</option>
        <option value="ingredients">Ingredients</option>
      </select>
      <button onClick={handleSearch}>Search</button>
      <div className="recipe-list">
        {results.map(recipe => (
          <div key={recipe.id} className="recipe-item">
            <h3>{recipe.name}</h3>
            <p>{recipe.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Search;
