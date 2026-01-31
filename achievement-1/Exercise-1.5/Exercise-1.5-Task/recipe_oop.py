class Recipe:
    # Class variable to store all ingredients across recipes
    all_ingredients = []

    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = 0
        self.difficulty = None

    # Getter and setter for name
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    # Getter and setter for cooking time
    def get_cooking_time(self):
        return self.cooking_time

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time
        self.difficulty = None  # reset difficulty if cooking time changes

    # Add ingredients using variable-length arguments
    def add_ingredients(self, *args):
        for ingredient in args:
            self.ingredients.append(ingredient)
        self.update_all_ingredients()
        self.difficulty = None  # reset difficulty if ingredients change

    # Update class-level ingredient list
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)

    # Calculate difficulty based on rules
    def calculate_difficulty(self):
        if self.cooking_time < 10:
            if len(self.ingredients) < 4:
                self.difficulty = "Easy"
            else:
                self.difficulty = "Medium"
        else:
            if len(self.ingredients) < 4:
                self.difficulty = "Intermediate"
            else:
                self.difficulty = "Hard"

    # Getter for difficulty (lazy evaluation)
    def get_difficulty(self):
        if self.difficulty is None:
            self.calculate_difficulty()
        return self.difficulty

    # Search for an ingredient in this recipe
    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

    # String representation of the recipe
    def __str__(self):
        ingredients_str = ", ".join(self.ingredients)
        return (
            f"Recipe: {self.name}\n"
            f"Cooking Time: {self.cooking_time} minutes\n"
            f"Ingredients: {ingredients_str}\n"
            f"Difficulty: {self.get_difficulty()}\n"
        )


# Function to search recipes by ingredient
def recipe_search(data, search_term):
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)


# -------- MAIN SCRIPT --------

# Tea
tea = Recipe("Tea")
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
tea.set_cooking_time(5)
print(tea)

# Coffee
coffee = Recipe("Coffee")
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
coffee.set_cooking_time(5)
print(coffee)

# Cake
cake = Recipe("Cake")
cake.add_ingredients(
    "Sugar", "Butter", "Eggs", "Vanilla Essence",
    "Flour", "Baking Powder", "Milk"
)
cake.set_cooking_time(50)
print(cake)

# Banana Smoothie
banana_smoothie = Recipe("Banana Smoothie")
banana_smoothie.add_ingredients(
    "Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"
)
banana_smoothie.set_cooking_time(5)
print(banana_smoothie)

# Wrap recipes into a list
recipes_list = [tea, coffee, cake, banana_smoothie]

# Search for recipes by ingredient
print("Recipes with Water:")
recipe_search(recipes_list, "Water")

print("Recipes with Sugar:")
recipe_search(recipes_list, "Sugar")

print("Recipes with Bananas:")
recipe_search(recipes_list, "Bananas")
