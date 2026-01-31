from sqlalchemy import create_engine, Column
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.types import Integer, String
import os

Base = declarative_base()

# ------------------ MODEL ------------------

class Recipe(Base):
    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return f"<Recipe ID: {self.id} - {self.name}>"

    def __str__(self):
        return (
            f"\nRecipe ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Ingredients: {self.ingredients}\n"
            f"Cooking Time: {self.cooking_time} minutes\n"
            f"Difficulty: {self.difficulty}\n"
        )

    def calculate_difficulty(self):
        ingredients_list = self.return_ingredients_as_list()

        if self.cooking_time < 10 and len(ingredients_list) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(ingredients_list) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(ingredients_list) < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    def return_ingredients_as_list(self):
        if not self.ingredients:
            return []
        return self.ingredients.split(", ")

# ------------------ CRUD FUNCTIONS ------------------

def create_recipe(session):
    name = input("Enter recipe name: ").strip()

    if len(name) == 0 or len(name) > 50:
        print("Invalid recipe name.")
        return

    cooking_time = input("Enter cooking time (minutes): ")
    if not cooking_time.isnumeric():
        print("Cooking time must be a number.")
        return

    cooking_time = int(cooking_time)

    ingredients = []
    count = input("How many ingredients? ")

    if not count.isnumeric():
        print("Invalid number.")
        return

    for i in range(int(count)):
        ingredient = input(f"Ingredient {i+1}: ").strip()
        if ingredient:
            ingredients.append(ingredient)

    ingredients_str = ", ".join(ingredients)

    recipe = Recipe(
        name=name,
        ingredients=ingredients_str,
        cooking_time=cooking_time
    )

    recipe.calculate_difficulty()

    session.add(recipe)
    session.commit()

    print("Recipe added successfully!")





def update_recipe(session):
    recipe_id = input("Enter recipe ID to update: ")

    if not recipe_id.isnumeric():
        print("Invalid ID")
        return

    recipe_id = int(recipe_id)
    recipe = session.get(Recipe, recipe_id)

    if recipe is None:
        print("Recipe not found")
        return

    print(recipe)

    print("1. Name\n2. Cooking Time\n3. Ingredients")
    choice = input("Choose field to update: ")

    if choice == "1":
        recipe.name = input("Enter new name: ")

    elif choice == "2":
        new_time = input("Enter new cooking time: ")
        if not new_time.isnumeric():
            print("Invalid cooking time")
            return
        recipe.cooking_time = int(new_time)

    elif choice == "3":
        ingredients = []
        count = input("How many ingredients? ")

        if not count.isnumeric():
            print("Invalid number")
            return

        for i in range(int(count)):
            ingredients.append(input(f"Ingredient {i+1}: "))

        recipe.ingredients = ", ".join(ingredients)

    else:
        print("Invalid choice")
        return

    recipe.calculate_difficulty()
    session.commit()
    print("Recipe updated successfully!")


def search_by_ingredients(session):
    if session.query(Recipe).count() == 0:
        print("No recipes available.")
        return

    results = session.query(Recipe.ingredients).all()

    all_ingredients = []

    for row in results:
        ingredient_list = row[0].split(", ")
        for ingredient in ingredient_list:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)

    print("\nAvailable ingredients:")
    for i, ingredient in enumerate(all_ingredients, start=1):
        print(f"{i}. {ingredient}")

    choices = input(
        "\nEnter ingredient numbers separated by spaces (e.g. 1 3): "
    ).split()

    if not all(choice.isnumeric() for choice in choices):
        print("Invalid input.")
        return

    search_ingredients = [
        all_ingredients[int(choice) - 1]
        for choice in choices
        if 0 < int(choice) <= len(all_ingredients)
    ]

    if not search_ingredients:
        print("No valid ingredients selected.")
        return

    conditions = [
        Recipe.ingredients.like(f"%{ingredient}%")
        for ingredient in search_ingredients
    ]

    recipes = session.query(Recipe).filter(*conditions).all()

    if not recipes:
        print("No recipes found.")
        return

    for recipe in recipes:
        print(recipe)



def delete_recipe(session):
    recipe_id = int(input("Enter recipe ID to delete: "))
    recipe = session.get(Recipe, recipe_id)

    if recipe is None:
        print("Recipe not found")
        return

    print(recipe)
    confirm = input("Confirm delete (yes/no): ")

    if confirm.lower() == "yes":
        session.delete(recipe)
        session.commit()
        print("Recipe deleted!")
    else:
        print("Delete cancelled.")


def view_all_recipes(session):
    recipes = session.query(Recipe).all()

    if not recipes:
        print("No recipes found.")
        return

    for recipe in recipes:
        print(recipe)


# ------------------ MAIN MENU ------------------

def main_menu(session):
    while True:
        print("\n" + "=" * 35)
        print("RECIPE APPLICATION")
        print("=" * 35)
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search recipes by ingredient")
        print("4. Update a recipe")
        print("5. Delete a recipe")
        print("6. Quit")

        choice = input("\nEnter your choice (1–6): ")

        if choice == "1":
            create_recipe(session)

        elif choice == "2":
            view_all_recipes(session)

        elif choice == "3":
            search_by_ingredients(session)

        elif choice == "4":
            update_recipe(session)

        elif choice == "5":
            delete_recipe(session)

        elif choice == "6":
            print("Goodbye! 👋")
            session.close()
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# ------------------ DATABASE SETUP ------------------

DB_USER = os.getenv("DB_USER", "cf-python")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = "task_database"

engine = create_engine(
    f"mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ------------------ START APP ------------------
if __name__ == "__main__":
    main_menu(session)
