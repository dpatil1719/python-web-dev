# Initialize empty lists
recipes_list = []
ingredients_list = []

def take_recipe():
    name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter cooking time (in minutes): "))

    count = int(input("Enter the number of ingredients: "))
    ingredients = []

    for i in range(count):
        ingredient = input("Enter an ingredient: ")
        ingredients.append(ingredient)

    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients
    }

    return recipe

# Ask user how many recipes to enter
n = int(input("How many recipes would you like to enter? "))

for i in range(n):
    recipe = take_recipe()

    for ingredient in recipe["ingredients"]:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)

    recipes_list.append(recipe)

# Display recipes with difficulty
for recipe in recipes_list:
    cooking_time = recipe["cooking_time"]
    num_ingredients = len(recipe["ingredients"])

    if cooking_time < 10 and num_ingredients < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = "Intermediate"
    else:
        difficulty = "Hard"

    print("\nRecipe:", recipe["name"])
    print("Cooking Time:", cooking_time, "minutes")
    print("Ingredients:", recipe["ingredients"])
    print("Difficulty:", difficulty)

# Display all ingredients alphabetically
ingredients_list.sort()

print("\nIngredients Available Across All Recipes:")
for ingredient in ingredients_list:
    print(ingredient)
