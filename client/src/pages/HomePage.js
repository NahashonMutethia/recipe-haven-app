import React, { useState, useEffect } from 'react';
import RecipeList from '../components/Recipe/RecipeList';
import Search from '../components/Recipe/Search';
import Pagination from '../components/Recipe/Pagination';

function HomePage() {
  const [recipes, setRecipes] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);

  useEffect(() => {
    const fetchRecipes = async () => {
      try {
        const response = await fetch(`http://localhost:5000/recipes?page=${currentPage}`);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        setRecipes(data.recipes);
        setTotalPages(data.totalPages);
      } catch (error) {
        console.error('Error:', error);
      }
    };

    fetchRecipes();
  }, [currentPage]);

  const handleSearch = async (query) => {
    try {
      const response = await fetch(`http://localhost:5000/recipes/search?query=${query}`);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      setRecipes(data.recipes);
      setTotalPages(data.totalPages);
      setCurrentPage(1);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handlePageChange = (page) => {
    setCurrentPage(page);
  };

  return (
    <div className="home-page">
      <Search onSearch={handleSearch} />
      <RecipeList recipes={recipes} />
      <Pagination currentPage={currentPage} totalPages={totalPages} onPageChange={handlePageChange} />
    </div>
  );
}

export default HomePage;
