from lib.recipe import Recipe

class RecipeRepository:

    def __init__(self, connection):
        self._connection = connection

    # Retrieve all recipes
    def all(self):
        rows = self._connection.execute('SELECT * from recipes')
        recipes = []
        for row in rows:
            item = Recipe(row["id"], row["dish_name"], row["cooking_time"], row['rating'])
            recipes.append(item)
        return recipes
    
    # Find a single recipe by is id
    def find(self, recipe_id):
        rows = self._connection.execute(
            'SELECT * from recipes WHERE id = %s', [recipe_id])
        row = rows[0]
        return Recipe(row["id"], row["dish_name"], row["cooking_time"], row['rating'])
    

    