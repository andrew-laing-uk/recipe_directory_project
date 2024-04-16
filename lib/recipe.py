class Recipe:
    def __init__(self, dish_id, dish_name, cooking_time, rating):
        self.id = dish_id
        self.dish_name = dish_name
        self.cooking_time = cooking_time
        self.rating = rating

    def __repr__(self):
        return f"Recipe({self.id}, {self.dish_name}, {self.cooking_time}, {self.rating})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__