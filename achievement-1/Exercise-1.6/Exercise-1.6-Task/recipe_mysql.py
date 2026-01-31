import mysql.connector
import os

# -------------------------
# DATABASE CONNECTION
# -------------------------
try:
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "cf-python"),
        password=os.getenv("DB_PASSWORD", "password"),
        database="task_database"
    )
    cursor = conn.cursor()
except mysql.connector.Error as err:
    print("Error connecting to database:", err)
    exit()

# -------------------------
# DATABASE & TABLE SETUP
# -------------------------
try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
    cursor.execute("USE task_database")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Recipes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        ingredients VARCHAR(255),
        cooking_time INT,
        difficulty VARCHAR(20)
    )
    """)
except mysql.connector.Error as err:
    print("Database setup error:", err)

# -------------------------
# DIFFICULTY LOGIC
# -------------------------
def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        return "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        return "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        return "Intermediate"
    else:
        return "Hard"

# -------------------------
# CREATE RECIPE
# -------------------------
def create_recipe(conn, cursor):
    try:
        name = input("Enter recipe name: ")
        cooking_time = int(input("Enter cooking time (minutes): "))

        ingredients = []
        num = int(input("Enter number of ingredients: "))

        for i in range(num):
            ingredient = input(f"Enter ingredient {i + 1}: ")
            ingredients.append(ingredient)

        difficulty = calculate_difficulty(cooking_time, ingredients)
        ingredients_str = ", ".join(ingredients)

        cursor.execute(
            "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)",
            (name, ingredients_str, cooking_time, difficulty)
        )
        conn.commit()
        print("Recipe added successfully!")

    except ValueError:
        print("Invalid input. Please enter numbers where required.")
    except mysql.connector.Error as err:
        print("Database error:", err)

# -------------------------
# SEARCH RECIPE
# -------------------------
def search_recipe(conn, cursor):
    try:
        cursor.execute("SELECT ingredients FROM Recipes")
        results = cursor.fetchall()

        all_ingredients = []

        for row in results:
            ingredients = row[0].split(", ")
            for ingredient in ingredients:
                if ingredient not in all_ingredients:
                    all_ingredients.append(ingredient)

        if not all_ingredients:
            print("No ingredients found.")
            return

        print("\nAvailable ingredients:")
        for i, ingredient in enumerate(all_ingredients, start=1):
            print(f"{i}. {ingredient}")

        choice = int(input("Select ingredient number: "))
        search_ingredient = all_ingredients[choice - 1]

        cursor.execute(
            "SELECT name, ingredients, cooking_time, difficulty FROM Recipes WHERE ingredients LIKE %s",
            (f"%{search_ingredient}%",)
        )
        results = cursor.fetchall()

        print("\nRecipes containing", search_ingredient)
        for row in results:
            print(f"\nName: {row[0]}")
            print(f"Ingredients: {row[1]}")
            print(f"Cooking time: {row[2]} minutes")
            print(f"Difficulty: {row[3]}")

    except (ValueError, IndexError):
        print("Invalid selection.")
    except mysql.connector.Error as err:
        print("Database error:", err)

# -------------------------
# UPDATE RECIPE
# -------------------------
def update_recipe(conn, cursor):
    try:
        cursor.execute("SELECT id, name FROM Recipes")
        results = cursor.fetchall()

        if not results:
            print("No recipes available.")
            return

        print("\nAvailable recipes:")
        for row in results:
            print(f"{row[0]}. {row[1]}")

        recipe_id = int(input("Enter recipe ID to update: "))

        print("\nWhat do you want to update?")
        print("1. Name")
        print("2. Cooking time")
        print("3. Ingredients")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            new_name = input("Enter new name: ")
            cursor.execute(
                "UPDATE Recipes SET name = %s WHERE id = %s",
                (new_name, recipe_id)
            )

        elif choice == "2":
            new_time = int(input("Enter new cooking time: "))

            cursor.execute(
                "SELECT ingredients FROM Recipes WHERE id = %s",
                (recipe_id,)
            )
            ingredients = cursor.fetchone()[0].split(", ")
            new_difficulty = calculate_difficulty(new_time, ingredients)

            cursor.execute(
                "UPDATE Recipes SET cooking_time = %s, difficulty = %s WHERE id = %s",
                (new_time, new_difficulty, recipe_id)
            )

        elif choice == "3":
            ingredients = []
            num = int(input("Enter number of ingredients: "))

            for i in range(num):
                ingredient = input(f"Enter ingredient {i + 1}: ")
                ingredients.append(ingredient)

            ingredients_str = ", ".join(ingredients)

            cursor.execute(
                "SELECT cooking_time FROM Recipes WHERE id = %s",
                (recipe_id,)
            )
            cooking_time = cursor.fetchone()[0]
            new_difficulty = calculate_difficulty(cooking_time, ingredients)

            cursor.execute(
                "UPDATE Recipes SET ingredients = %s, difficulty = %s WHERE id = %s",
                (ingredients_str, new_difficulty, recipe_id)
            )
        else:
            print("Invalid choice.")
            return

        conn.commit()
        print("Recipe updated successfully!")

    except (ValueError, TypeError):
        print("Invalid input.")
    except mysql.connector.Error as err:
        print("Database error:", err)

# -------------------------
# DELETE RECIPE
# -------------------------
def delete_recipe(conn, cursor):
    try:
        cursor.execute("SELECT id, name FROM Recipes")
        results = cursor.fetchall()

        if not results:
            print("No recipes to delete.")
            return

        print("\nAvailable recipes:")
        for row in results:
            print(f"{row[0]}. {row[1]}")

        recipe_id = int(input("Enter recipe ID to delete: "))

        cursor.execute(
            "DELETE FROM Recipes WHERE id = %s",
            (recipe_id,)
        )
        conn.commit()
        print("Recipe deleted successfully!")

    except ValueError:
        print("Invalid ID.")
    except mysql.connector.Error as err:
        print("Database error:", err)

# -------------------------
# MAIN MENU
# -------------------------
def main_menu(conn, cursor):
    while True:
        print("\n--- Recipe Database Menu ---")
        print("1. Create recipe")
        print("2. Search recipe")
        print("3. Update recipe")
        print("4. Delete recipe")
        print("5. Quit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

# -------------------------
# RUN PROGRAM
# -------------------------
main_menu(conn, cursor)

cursor.close()
conn.close()
