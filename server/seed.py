from app import create_app, db
from app.models import Recipe

def seed_recipes():
    recipes_data = [
        {
            "name": "Spaghetti Carbonara",
            "description": "A classic Italian pasta dish made with eggs, cheese, pancetta, and pepper.",
            "ingredients": "Spaghetti, eggs, cheese, pancetta, pepper",
            "instructions": "1. Cook spaghetti. 2. Cook pancetta. 3. Mix eggs and cheese. 4. Combine all ingredients.",
            "main_photo": "https://images.pexels.com/photos/466675/pexels-photo-466675.jpeg",
            "step_photos": [
                "https://images.pexels.com/photos/466676/pexels-photo-466676.jpeg",
                "https://images.pexels.com/photos/466677/pexels-photo-466677.jpeg"
            ],
            "ingredient_photos": [
                "https://images.pexels.com/photos/467116/pexels-photo-467116.jpeg",
                "https://images.pexels.com/photos/466683/pexels-photo-466683.jpeg"
            ],
            "user_id": 1
        },
        {
            "name": "Chicken Tikka Masala",
            "description": "A popular Indian dish featuring marinated chicken in a creamy tomato sauce.",
            "ingredients": "Chicken, yogurt, spices, tomato sauce",
            "instructions": "1. Marinate chicken. 2. Cook chicken. 3. Prepare sauce. 4. Combine and simmer.",
            "main_photo": "https://images.pexels.com/photos/775678/pexels-photo-775678.jpeg",
            "step_photos": [
                "https://images.pexels.com/photos/775676/pexels-photo-775676.jpeg",
                "https://images.pexels.com/photos/775674/pexels-photo-775674.jpeg"
            ],
            "ingredient_photos": [
                "https://images.pexels.com/photos/2124524/pexels-photo-2124524.jpeg",
                "https://images.pexels.com/photos/3755066/pexels-photo-3755066.jpeg"
            ],
            "user_id": 1
        },
        {
            "name": "Beef Stroganoff",
            "description": "A creamy beef dish with mushrooms and onions, served over egg noodles.",
            "ingredients": "Beef, mushrooms, onions, sour cream",
            "instructions": "1. Brown beef. 2. Sauté mushrooms and onions. 3. Combine with beef. 4. Add sour cream and serve.",
            "main_photo": "https://images.pexels.com/photos/3584391/pexels-photo-3584391.jpeg",
            "step_photos": [
                "https://images.pexels.com/photos/3584392/pexels-photo-3584392.jpeg",
                "https://images.pexels.com/photos/3584393/pexels-photo-3584393.jpeg"
            ],
            "ingredient_photos": [
                "https://images.pexels.com/photos/4164900/pexels-photo-4164900.jpeg",
                "https://images.pexels.com/photos/4173508/pexels-photo-4173508.jpeg"
            ],
            "user_id": 1
        },
        {
            "name": "Vegetable Stir-Fry",
            "description": "A quick and healthy stir-fry with mixed vegetables and a savory sauce.",
            "ingredients": "Mixed vegetables, soy sauce, garlic, ginger",
            "instructions": "1. Chop vegetables. 2. Stir-fry with garlic and ginger. 3. Add soy sauce and serve.",
            "main_photo": "https://images.pexels.com/photos/2091511/pexels-photo-2091511.jpeg",
            "step_photos": [
                "https://images.pexels.com/photos/2091509/pexels-photo-2091509.jpeg",
                "https://images.pexels.com/photos/2091510/pexels-photo-2091510.jpeg"
            ],
            "ingredient_photos": [
                "https://images.pexels.com/photos/1630795/pexels-photo-1630795.jpeg",
                "https://images.pexels.com/photos/1611747/pexels-photo-1611747.jpeg"
            ],
            "user_id": 1
        },
        {
            "name": "Tacos",
            "description": "Delicious Mexican tacos with seasoned beef and fresh toppings.",
            "ingredients": "Ground beef, taco seasoning, tortillas, lettuce, cheese",
            "instructions": "1. Cook beef with seasoning. 2. Warm tortillas. 3. Assemble tacos with toppings.",
            "main_photo": "https://images.pexels.com/photos/776482/pexels-photo-776482.jpeg",
            "step_photos": [
                "https://images.pexels.com/photos/776481/pexels-photo-776481.jpeg",
                "https://images.pexels.com/photos/776480/pexels-photo-776480.jpeg"
            ],
            "ingredient_photos": [
                "https://images.pexels.com/photos/2865778/pexels-photo-2865778.jpeg",
                "https://images.pexels.com/photos/2824259/pexels-photo-2824259.jpeg"
            ],
            "user_id": 1
        },
        {
            "name": "Caesar Salad",
            "description": "A classic Caesar salad with romaine lettuce, croutons, and Caesar dressing.",
            "ingredients": "Romaine lettuce, croutons, Caesar dressing, Parmesan cheese",
            "instructions": "1. Chop lettuce. 2. Toss with croutons and cheese. 3. Add dressing and serve.",
            "main_photo": "https://images.pexels.com/photos/1153327/pexels-photo-1153327.jpeg",
            "step_photos": [
                "https://images.pexels.com/photos/1153326/pexels-photo-1153326.jpeg",
                "https://images.pexels.com/photos/1153325/pexels-photo-1153325.jpeg"
            ],
            "ingredient_photos": [
                "https://images.pexels.com/photos/3826596/pexels-photo-3826596.jpeg",
                "https://images.pexels.com/photos/1756359/pexels-photo-1756359.jpeg"
            ],
            "user_id": 1
        },
        {
            "name": "Chocolate Chip Cookies",
            "description": "Soft and chewy chocolate chip cookies with a golden edge.",
            "ingredients": "Flour, butter, sugar, chocolate chips",
            "instructions": "1. Mix ingredients. 2. Form dough into cookies. 3. Bake until golden.",
            "main_photo": "https://images.pexels.com/photos/238609/pexels-photo-238609.jpeg",
            "step_photos": [
                "https://images.pexels.com/photos/238610/pexels-photo-238610.jpeg",
                "https://images.pexels.com/photos/238612/pexels-photo-238612.jpeg"
            ],
            "ingredient_photos": [
                "https://images.pexels.com/photos/238611/pexels-photo-238611.jpeg",
                "https://images.pexels.com/photos/238613/pexels-photo-238613.jpeg"
            ],
            "user_id": 1
        },
        {
            "name": "Grilled Salmon",
            "description": "A simple and healthy grilled salmon with lemon and herbs.",
            "ingredients": "Salmon, lemon, herbs, olive oil",
            "instructions": "1. Season salmon. 2. Grill with lemon and herbs. 3. Serve with a side.",
            "main_photo": "https://images.pexels.com/photos/2727435/pexels-photo-2727435.jpeg",
            "step_photos": [
                "https://images.pexels.com/photos/2727438/pexels-photo-2727438.jpeg",
                "https://images.pexels.com/photos/2727436/pexels-photo-2727436.jpeg"
            ],
            "ingredient_photos": [
                "https://images.pexels.com/photos/4158552/pexels-photo-4158552.jpeg",
                "https://images.pexels.com/photos/4197418/pexels-photo-4197418.jpeg"
            ],
            "user_id": 1
        },
        {
            "name": "Pancakes",
            "description": "Fluffy and light pancakes perfect for breakfast.",
            "ingredients": "Flour, eggs, milk, baking powder",
            "instructions": "1. Mix ingredients. 2. Cook on griddle. 3. Serve with syrup.",
            "main_photo": "https://images.pexels.com/photos/580263/pexels-photo-580263.jpeg",
            "step_photos": [
                "https://images.pexels.com/photos/580268/pexels-photo-580268.jpeg",
                "https://images.pexels.com/photos/580260/pexels-photo-580260.jpeg"
            ],
            "ingredient_photos": [
                "https://images.pexels.com/photos/212052/pexels-photo-212052.jpeg",
                "https://images.pexels.com/photos/1385369/pexels-photo-1385369.jpeg"
            ],
            "user_id": 1
        },
        {
            "name": "Greek Salad",
            "description": "A refreshing Greek salad with tomatoes, cucumbers, olives, and feta cheese.",
            "ingredients": "Tomatoes, cucumbers, olives, feta cheese",
            "instructions": "1. Chop vegetables. 2. Toss with olives and feta. 3. Add dressing and serve.",
            "main_photo": "https://images.pexels.com/photos/1122417/pexels-photo-1122417.jpeg",
            "step_photos": [
                "https://images.pexels.com/photos/1122416/pexels-photo-1122416.jpeg",
                "https://images.pexels.com/photos/1122415/pexels-photo-1122415.jpeg"
            ],
            "ingredient_photos": [
                "https://images.pexels.com/photos/4859505/pexels-photo-4859505.jpeg",
                "https://images.pexels.com/photos/3807737/pexels-photo-3807737.jpeg"
            ],
            "user_id": 1
        },
        {
            "name": "Margarita Pizza",
            "description": "A classic pizza with fresh tomato sauce, mozzarella cheese, and basil.",
            "ingredients": "Pizza dough, tomato sauce, mozzarella cheese, basil",
            "instructions": "1. Prepare dough. 2. Spread sauce. 3. Add cheese and basil. 4. Bake until golden.",
            "main_photo": "https://images.pexels.com/photos/4197356/pexels-photo-4197356.jpeg",
            "step_photos": [
                "https://images.pexels.com/photos/4197358/pexels-photo-4197358.jpeg",
                "https://images.pexels.com/photos/4197362/pexels-photo-4197362.jpeg"
            ],
            "ingredient_photos": [
                "https://images.pexels.com/photos/1640776/pexels-photo-1640776.jpeg",
                "https://images.pexels.com/photos/2092909/pexels-photo-2092909.jpeg"
            ],
            "user_id": 1
        },
        {
            "name": "Lemonade",
            "description": "Refreshing lemonade made with freshly squeezed lemons and sugar.",
            "ingredients": "Lemons, sugar, water",
            "instructions": "1. Squeeze lemons. 2. Mix with sugar and water. 3. Chill and serve.",
            "main_photo": "https://images.pexels.com/photos/1347364/pexels-photo-1347364.jpeg",
            "step_photos": [
                "https://images.pexels.com/photos/1347365/pexels-photo-1347365.jpeg",
                "https://images.pexels.com/photos/1347367/pexels-photo-1347367.jpeg"
            ],
            "ingredient_photos": [
                "https://images.pexels.com/photos/1057245/pexels-photo-1057245.jpeg",
                "https://images.pexels.com/photos/1104677/pexels-photo-1104677.jpeg"
            ],
            "user_id": 1
        }
    ]

    with create_app().app_context():
        db.create_all()
        for recipe_data in recipes_data:
            recipe = Recipe(
                name=recipe_data['name'],
                description=recipe_data['description'],
                ingredients=recipe_data['ingredients'],
                instructions=recipe_data['instructions'],
                main_photo=recipe_data['main_photo'],
                step_photos=recipe_data['step_photos'],
                ingredient_photos=recipe_data['ingredient_photos'],
                user_id=recipe_data['user_id']
            )
            db.session.add(recipe)
        db.session.commit()

if __name__ == "__main__":
    seed_recipes()
