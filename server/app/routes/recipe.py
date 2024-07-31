from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Recipe, User, Review, Favorite

recipe = Blueprint('recipe', __name__)

@recipe.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    return jsonify([{
        'id': recipe.id,
        'name': recipe.name,
        'description': recipe.description,
        'ingredients': recipe.ingredients,
        'instructions': recipe.instructions
    } for recipe in recipes])

@recipe.route('/recipes', methods=['POST'])
@jwt_required()
def add_recipe():
    data = request.get_json()
    current_user_id = get_jwt_identity()
    new_recipe = Recipe(
        name=data['name'],
        description=data['description'],
        ingredients=data['ingredients'],
        instructions=data['instructions'],
        user_id=current_user_id
    )
    db.session.add(new_recipe)
    db.session.commit()
    return jsonify({"message": "Recipe added successfully"}), 201

@recipe.route('/recipes/<int:recipe_id>', methods=['PUT'])
@jwt_required()
def update_recipe(recipe_id):
    data = request.get_json()
    current_user_id = get_jwt_identity()
    recipe = Recipe.query.filter_by(id=recipe_id, user_id=current_user_id).first()

    if not recipe:
        return jsonify({"message": "Recipe not found or not authorized"}), 404

    recipe.name = data.get('name', recipe.name)
    recipe.description = data.get('description', recipe.description)
    recipe.ingredients = data.get('ingredients', recipe.ingredients)
    recipe.instructions = data.get('instructions', recipe.instructions)

    db.session.commit()
    return jsonify({"message": "Recipe updated successfully"}), 200

@recipe.route('/recipes/<int:recipe_id>', methods=['DELETE'])
@jwt_required()
def delete_recipe(recipe_id):
    current_user_id = get_jwt_identity()
    recipe = Recipe.query.filter_by(id=recipe_id, user_id=current_user_id).first()

    if not recipe:
        return jsonify({"message": "Recipe not found or not authorized"}), 404

    db.session.delete(recipe)
    db.session.commit()
    return jsonify({"message": "Recipe deleted successfully"}), 200

@recipe.route('/recipes/<int:recipe_id>/reviews', methods=['POST'])
@jwt_required()
def add_review(recipe_id):
    data = request.get_json()
    current_user_id = get_jwt_identity()
    new_review = Review(
        rating=data['rating'],
        comment=data['comment'],
        user_id=current_user_id,
        recipe_id=recipe_id
    )
    db.session.add(new_review)
    db.session.commit()
    return jsonify({"message": "Review added successfully"}), 201

@recipe.route('/recipes/<int:recipe_id>/reviews', methods=['GET'])
def get_reviews(recipe_id):
    reviews = Review.query.filter_by(recipe_id=recipe_id).all()
    return jsonify([{
        'id': review.id,
        'rating': review.rating,
        'comment': review.comment,
        'created_at': review.created_at
    } for review in reviews])
