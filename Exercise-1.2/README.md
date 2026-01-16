# Exercise 1.2 — Data Types in Python (Recipe App)

## Data structure choice for a recipe (50–75 words)
I used a dictionary for each recipe because a recipe has clearly labeled attributes (name, cooking_time, ingredients). Using keys makes the structure easy to read and access, for example recipe["ingredients"]. Dictionaries are also flexible: if I want to add new attributes later (like servings, difficulty, or cuisine), I can do so without changing the overall structure.

## Data structure choice for all_recipes
I used a list for all_recipes because it stores multiple recipes in a sequential order and makes it easy to add, remove, or modify recipes. A list works well for iterating through recipes and printing information such as ingredients for each recipe.
