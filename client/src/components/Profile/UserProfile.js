import React, { useState, useEffect } from 'react';
import { getToken } from '../../utils';
import './Profile.css';

function UserProfile() {
  const [user, setUser] = useState(null);
  const [favorites, setFavorites] = useState([]);
  const [wishlist, setWishlist] = useState([]);
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const response = await fetch('http://localhost:5000/users/profile', {
          headers: {
            'Authorization': `Bearer ${getToken()}`,
          },
        });

        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        const data = await response.json();
        setUser(data);
      } catch (error) {
        console.error('Error:', error);
      }
    };

    const fetchFavorites = async () => {
      try {
        const response = await fetch('http://localhost:5000/users/favorites', {
          headers: {
            'Authorization': `Bearer ${getToken()}`,
          },
        });

        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        const data = await response.json();
        setFavorites(data);
      } catch (error) {
        console.error('Error:', error);
      }
    };

    const fetchWishlist = async () => {
      try {
        const response = await fetch('http://localhost:5000/users/wishlist', {
          headers: {
            'Authorization': `Bearer ${getToken()}`,
          },
        });

        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        const data = await response.json();
        setWishlist(data);
      } catch (error) {
        console.error('Error:', error);
      }
    };

    const fetchRecommendations = async () => {
      try {
        const response = await fetch('http://localhost:5000/users/recommendations', {
          headers: {
            'Authorization': `Bearer ${getToken()}`,
          },
        });

        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        const data = await response.json();
        setRecommendations(data);
      } catch (error) {
        console.error('Error:', error);
      }
    };

    fetchUser();
    fetchFavorites();
    fetchWishlist();
    fetchRecommendations();
  }, []);

  if (!user) return <div>Loading...</div>;

  return (
    <div className="user-profile">
      <h2>{user.username}</h2>
      <p>Email: {user.email}</p>
      <img src={`http://localhost:5000/uploads/${user.profile_photo}`} alt="Profile" />

      <h3>Favorite Recipes</h3>
      <ul>
        {favorites.map((recipe) => (
          <li key={recipe.id}>{recipe.name}</li>
        ))}
      </ul>

      <h3>Wishlist</h3>
      <ul>
        {wishlist.map((recipe) => (
          <li key={recipe.id}>{recipe.name}</li>
        ))}
      </ul>

      <h3>Recommended Recipes</h3>
      <ul>
        {recommendations.map((rec) => (
          <li key={rec.id}>
            {rec.name} - {rec.reason}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default UserProfile;
