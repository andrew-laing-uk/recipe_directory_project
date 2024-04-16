from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

"""
When we call RecipeRepository#all
We get a list of Recipe objects reflecting the seed data.
"""
def test_get_all_records(db_connection): 
    db_connection.seed("seeds/recipes.sql") 
    repository = RecipeRepository(db_connection)
    recipes = repository.all()
    assert recipes == [
        Recipe(1, 'Creamy Vegan Pasta', 120, 4),
        Recipe(2, 'Cold Noodles with Roasted Tomatoes', 45, 3),
        Recipe(3, 'Curried Jasmine Rice with Tofu and Vegetables', 90, 4),
        Recipe(4, 'Bucatini Pasta with Arugula Pesto', 100, 4),
        Recipe(5, 'Crispy BBQ Tofu Sandwich', 30, 5),
        Recipe(6, 'Morrocan Chickpea Salad', 40, 3),
        Recipe(7, 'Tamales', 20, 2),
        Recipe(8, 'Vegan Pozole', 60, 5),
        Recipe(9, 'Thick Soup with Beans', 60, 3),
        Recipe(10, 'Berry-tastic Desert', 40, 5),
    ]

"""
When we call RecipeRepository#find
We get a single Artist object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/recipes.sql") 
    repository = RecipeRepository(db_connection)
    recipe = repository.find(4)
    assert recipe == Recipe(4, 'Bucatini Pasta with Arugula Pesto', 100, 4)
