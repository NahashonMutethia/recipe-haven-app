from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.__init__ import db
from app.models import User, Favorite, Recipe

user = Blueprint('user', __name__)

@user.route('/user/profile', methods=['GET'])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email
    })

@user.route('/user/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    data = request.get_json()
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    db.session.commit()
    return jsonify({"message": "Profile updated successfully"}), 200

@user.route('/user/favorites', methods=['POST'])
@jwt_required()
def add_favorite():
    data = request.get_json()
    user_id = get_jwt_identity()
    recipe_id = data['recipe_id']

    favorite = Favorite(user_id=user_id, recipe_id=recipe_id)
    db.session.add(favorite)
    db.session.commit()
    return jsonify({"message": "Recipe added to favorites"}), 201

@user.route('/user/favorites', methods=['GET'])
@jwt_required()
def get_favorites():
    user_id = get_jwt_identity()
    favorites = Favorite.query.filter_by(user_id=user_id).all()
    favorite_recipes = [Recipe.query.get(fav.recipe_id) for fav in favorites]
    return jsonify([{
        'id': recipe.id,
        'name': recipe.name,
        'description': recipe.description
    } for recipe in favorite_recipes])
