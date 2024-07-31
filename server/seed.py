from app.__init__ import create_app
from app.__init__ import db
from app.models import User

# Create an application context
app = create_app()
app.app_context().push()

# Define a function to seed the database with initial data
def seed_database():
    # Create users
    user1 = User(username='alice', email='alice@example.com')
    user1.set_password('password123')

    user2 = User(username='bob', email='bob@example.com')
    user2.set_password('password456')

    user3 = User(username='charlie', email='charlie@example.com')
    user3.set_password('password789')

    # Add users to the session
    db.session.add_all([user1, user2, user3])

    # Commit the session to save the users to the database
    db.session.commit()
    print("Database seeded with initial users.")

# Drop all tables and recreate them
db.drop_all()
db.create_all()

# Seed the database
seed_database()
