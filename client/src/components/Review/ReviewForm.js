import React, { useState } from 'react';
import { getToken } from '../../utils';
import './Review.css';

function ReviewForm({ recipeId }) {
  const [comment, setComment] = useState('');
  const [rating, setRating] = useState(1);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch(`http://localhost:5000/recipes/${recipeId}/reviews`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${getToken()}`,
        },
        body: JSON.stringify({ comment, rating }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      setComment('');
      setRating(1);
      alert('Review submitted successfully');
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="review-form">
      <h3>Submit a Review</h3>
      <form onSubmit={handleSubmit}>
        <textarea
          placeholder="Comment"
          value={comment}
          onChange={(e) => setComment(e.target.value)}
          required
        ></textarea>
        <select
          value={rating}
          onChange={(e) => setRating(parseInt(e.target.value))}
          required
        >
          {[1, 2, 3, 4, 5].map((value) => (
            <option key={value} value={value}>
              {value}
            </option>
          ))}
        </select>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default ReviewForm;
