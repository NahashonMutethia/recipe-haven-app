from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os


db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

    db.init_app(app)
    jwt.init_app(app)
    CORS(app)
    
    with app.app_context():
        db.create_all() 

    from .routes.auth import auth
    from .routes.recipe import recipe
    from .routes.user import user
    
    app.register_blueprint(auth)
    app.register_blueprint(recipe)
    app.register_blueprint(user)

    return app
