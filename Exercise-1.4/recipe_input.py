import pickle

def calc_difficulty(cooking_time, num_ingredients):
    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    else:
        return "Hard"


def take_recipe():
    recipe_name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter the cooking time (minutes): "))
    num_ingredients = int(input("Enter number of ingredients: "))

    ingredients = []
    for i in range(num_ingredients):
        ingredient = input("Enter the ingredient: ")
        ingredients.append(ingredient)

    difficulty = calc_difficulty(cooking_time, len(ingredients))

    recipe = {
        "name": recipe_name,
        "cooking_time": cooking_time,
        "ingredients": ingredients,
        "difficulty": difficulty
    }

    return recipe


filename = input("Enter the filename to store recipes: ")

try:
    file = open(filename, "rb")
    data = pickle.load(file)
except FileNotFoundError:
    data = {
        "recipes_list": [],
        "all_ingredients": []
    }
except:
    data = {
        "recipes_list": [],
        "all_ingredients": []
    }
else:
    file.close()
finally:
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]


n = int(input("How many recipes would you like to enter? "))

for i in range(n):
    recipe = take_recipe()
    recipes_list.append(recipe)

    for ingredient in recipe["ingredients"]:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)


data["recipes_list"] = recipes_list
data["all_ingredients"] = all_ingredients

with open(filename, "wb") as file:
    pickle.dump(data, file)
