from app.__init__ import create_app, db
from app.models import User, Recipe, Review, Favorite

# Create an application context
app = create_app()
app.app_context().push()

# Define a function to seed the database with initial data
def seed_database():
    # Create new users
    user4 = User(username='david', email='david@example.com')
    user4.set_password('securepass1')

    user5 = User(username='eva', email='eva@example.com')
    user5.set_password('securepass2')

    user6 = User(username='frank', email='frank@example.com')
    user6.set_password('securepass3')

    # Add new users to the session
    db.session.add_all([user4, user5, user6])
    db.session.commit()

    # Create new recipes
    recipe4 = Recipe(
        name='Beef Stew',
        description='A hearty stew with tender beef and vegetables.',
        ingredients='Beef, carrots, potatoes, onions, celery, beef broth',
        instructions='1. Brown beef. 2. Add vegetables and broth. 3. Simmer until tender.',
        user_id=user4.id
    )
    recipe5 = Recipe(
        name='Vegetable Stir Fry',
        description='A colorful mix of vegetables stir-fried in a savory sauce.',
        ingredients='Broccoli, bell peppers, carrots, snow peas, soy sauce',
        instructions='1. Stir-fry vegetables. 2. Add soy sauce. 3. Serve hot.',
        user_id=user5.id
    )
    recipe6 = Recipe(
        name='Pancakes',
        description='Fluffy pancakes perfect for a weekend breakfast.',
        ingredients='Flour, milk, eggs, butter, baking powder, sugar',
        instructions='1. Mix ingredients. 2. Cook on griddle. 3. Serve with syrup.',
        user_id=user6.id
    )

    # Add new recipes to the session
    db.session.add_all([recipe4, recipe5, recipe6])
    db.session.commit()

    # Create new reviews
    review4 = Review(
        rating=5,
        comment='The beef stew was amazing and very filling!',
        user_id=user4.id,
        recipe_id=recipe4.id
    )
    review5 = Review(
        rating=4,
        comment='Great stir fry, but I would add more soy sauce next time.',
        user_id=user5.id,
        recipe_id=recipe5.id
    )
    review6 = Review(
        rating=5,
        comment='Pancakes were perfect! Just the right amount of fluffiness.',
        user_id=user6.id,
        recipe_id=recipe6.id
    )

    # Add new reviews to the session
    db.session.add_all([review4, review5, review6])
    db.session.commit()

    # Create new favorites
    favorite4 = Favorite(user_id=user4.id, recipe_id=recipe5.id)  # David likes Vegetable Stir Fry
    favorite5 = Favorite(user_id=user5.id, recipe_id=recipe6.id)  # Eva likes Pancakes
    favorite6 = Favorite(user_id=user6.id, recipe_id=recipe4.id)  # Frank likes Beef Stew

    # Add new favorites to the session
    db.session.add_all([favorite4, favorite5, favorite6])
    db.session.commit()

    print("Database seeded with new users, recipes, reviews, and favorites.")

# Drop all tables and recreate them
db.drop_all()
db.create_all()

# Seed the database
seed_database()
