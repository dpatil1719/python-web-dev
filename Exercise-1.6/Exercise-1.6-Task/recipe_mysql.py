import mysql.connector
conn = mysql.connector.connect(
    host ="localhost",
    user ="cf-python",
    password ="password"
)

cursor = conn.cursor()
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


def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        return "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        return "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        return "Intermediate"
    else:
        return "Hard"


def create_recipe(conn, cursor):
     name = input("Enter recipe name: ")

     cooking_time = int(input("Enter cooking time (in minutes): "))

     ingredients = []
     num_ingredients = int(input("How many ingredients? "))

     for i in range(num_ingredients):
        ingredient = input(f"Enter ingredient {i + 1}: ")
        ingredients.append(ingredient)

     ingredients_str = ", ".join(ingredients)

     difficulty = calculate_difficulty(cooking_time, ingredients)

     sql = """
     INSERT INTO Recipes (name, ingredients, cooking_time, difficulty)
     VALUES (%s, %s, %s, %s)
     """

     values = (name, ingredients_str, cooking_time, difficulty)
     cursor.execute(sql, values)
     conn.commit()

     print("Recipe added successfully!")


def search_recipe(conn, cursor):
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()

    all_ingredients = []

    for row in results:
        ingredients = row[0].split(", ")
        for ingredient in ingredients:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)

    print("\nAvailable ingredients:")
    for i, ingredient in enumerate(all_ingredients, start=1):
        print(f"{i}. {ingredient}")

    choice = int(input("Select an ingredient by number: "))
    search_ingredient = all_ingredients[choice - 1]

    sql = """
    SELECT name, ingredients, cooking_time, difficulty
    FROM Recipes
    WHERE ingredients LIKE %s
    """

    cursor.execute(sql, (f"%{search_ingredient}%",))
    results = cursor.fetchall()

    print("\nRecipes containing", search_ingredient)
    for row in results:
        print(f"\nName: {row[0]}")
        print(f"Ingredients: {row[1]}")
        print(f"Cooking time: {row[2]} minutes")
        print(f"Difficulty: {row[3]}")


def update_recipe(conn, cursor):
    cursor.execute("SELECT id, name FROM Recipes")
    results = cursor.fetchall()

    print("\nAvailable recipes:")
    for row in results:
        print(f"{row[0]}. {row[1]}")

    recipe_id = int(input("Enter the ID of the recipe you want to update: "))

    print("\nWhat do you want to update?")
    print("1. Name")
    print("2. Cooking time")
    print("3. Ingredients")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        new_name = input("Enter new recipe name: ")
        cursor.execute(
            "UPDATE Recipes SET name = %s WHERE id = %s",
            (new_name, recipe_id)
        )

    elif choice == "2":
        new_time = int(input("Enter new cooking time (minutes): "))

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
        num = int(input("How many ingredients? "))

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

    conn.commit()
    print("Recipe updated successfully!")



def delete_recipe(conn, cursor):
    cursor.execute("SELECT id, name FROM Recipes")
    results = cursor.fetchall()

    print("\nAvailable recipes:")
    for row in results:
        print(f"{row[0]}. {row[1]}")

    recipe_id = int(input("Enter the ID of the recipe you want to delete: "))

    cursor.execute(
        "DELETE FROM Recipes WHERE id = %s",
        (recipe_id,)
    )

    conn.commit()
    print("Recipe deleted successfully!")




def main_menu(conn,cursor):
    while True:
        print("\n--- Recipe Database Menu ---")
        print("1. Create a new recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

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
            print("Invalid choice. Please try again.")

main_menu(conn, cursor)



conn.commit()
cursor.close()
conn.close()

