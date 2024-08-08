import React from 'react';
import './Review.css';

function ReviewList({ reviews }) {
  return (
    <div className="review-list">
      <h3>Reviews</h3>
      {reviews.map((review) => (
        <div key={review.id} className="review-item">
          <p>{review.comment}</p>
          <p>Rating: {review.rating}</p>
        </div>
      ))}
    </div>
  );
}

export default ReviewList;
