import pickle

filename = input("Enter the filename to search recipes: ")

try:
    with open(filename, "rb") as file:
        data = pickle.load(file)
except FileNotFoundError:
    print("No recipe file found. Please add recipes first.")
    exit()
except:
    print("An unexpected error occurred while loading the file.")
    exit()

recipes_list = data["recipes_list"]
all_ingredients = data["all_ingredients"]


def search_ingredient(data):
    print("\nAvailable ingredients:")
    for index, ingredient in enumerate(data["all_ingredients"]):
        print(index, ingredient)

    try:
        choice = int(input("\nEnter the number of the ingredient to search: "))
        ingredient_searched = data["all_ingredients"][choice]
    except (ValueError, IndexError):
        print("Invalid selection. Please try again.")
        return
    else:
        print("\nRecipes containing", ingredient_searched + ":")

        found = False
        for recipe in data["recipes_list"]:
            if ingredient_searched in recipe["ingredients"]:
                found = True
                print("-" * 30)
                print("Name:", recipe["name"])
                print("Cooking time:", recipe["cooking_time"], "minutes")
                print("Difficulty:", recipe["difficulty"])
                print("Ingredients:", recipe["ingredients"])

        if not found:
            print("No recipes found with this ingredient.")


search_ingredient(data)
