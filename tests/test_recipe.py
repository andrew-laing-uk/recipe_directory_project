from lib.recipe import Recipe

"""
Recipe constructs with an id, dish_name, cooking_time and rating
"""
def test_recipe_constructs():
    recipe = Recipe(1, "Boiled Potatoes", 30, 4)
    assert recipe.id == 1
    assert recipe.dish_name == "Boiled Potatoes"
    assert recipe.cooking_time == 30
    assert recipe.rating == 4

"""
We can format recipes to strings nicely
"""
def test_recipes_format_nicely():
    recipe = Recipe(1, "Boiled Potatoes", 30, 4)
    assert str(recipe) == "Recipe(1, Boiled Potatoes, 30, 4)"

"""
We can compare two identical recipes
And have them be equal
"""
def test_artists_are_equal():
    recipe_1 = Recipe(1, "Boiled Potatoes", 30, 4)
    recipe_2 = Recipe(1, "Boiled Potatoes", 30, 4)
    assert recipe_1 == recipe_2