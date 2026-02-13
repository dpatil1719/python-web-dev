# Task-2.5 — Recipe Application (Exercise 2.5)

## 1. Model Review and Updates (from Exercise 2.3)

### Existing Model: `Recipe`

In Exercise 2.3, the Recipe model contained the following fields:

* `name` (CharField)
* `description` (TextField)
* `cooking_time` (IntegerField)
* `created_at` (DateTimeField)

### Changes Made in Exercise 2.5

To support images and frontend display requirements, the following updates were made:

* **Added image support**

  ```python
  pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')
  ```

  This allows each recipe to have an associated image. A default image (`no_picture.jpg`) is used when no image is uploaded.

* **Added difficulty calculation (method, not database field)**

  ```python
  def difficulty(self):
      if self.cooking_time < 10:
          return "Easy"
      elif self.cooking_time < 30:
          return "Medium"
      else:
          return "Hard"
  ```

  This method dynamically calculates recipe difficulty based on cooking time. It is intentionally not stored in the database.

### Reason for Changes

These changes were necessary to:

* Display recipe images on the frontend
* Compute and display recipe difficulty dynamically
* Meet the Exercise 2.5 requirements for media handling and business logic

---

## 2. Media Configuration

To support user-uploaded images, the following steps were completed:

* Created a `media/` folder at the project level
* Updated `settings.py`:

  ```python
  MEDIA_URL = '/media/'
  MEDIA_ROOT = BASE_DIR / 'media'
  ```
* Updated `recipe_project/urls.py` to serve media files during development:

  ```python
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```
* Added a default image file:

  ```
  src/media/no_picture.jpg
  ```

---

## 3. Adding Recipe Records

Using the Django admin panel (`/admin/`), at least **five recipes** were added, each with:

* Name
* Description
* Cooking time
* Image (or default image)

Examples include:

* Tomato Soup
* Pancakes
* Vegetable Biryani
* Vegetable Pasta
* Fruit Salad

---

## 4. Frontend Inspirations

### Selected Inspirations

* [https://www.allrecipes.com](https://www.allrecipes.com)
* [https://www.bbcgoodfood.com](https://www.bbcgoodfood.com)
* [https://www.delish.com](https://www.delish.com)

### Key Design Elements Inspired

* Clean list of recipes
* Clear cooking time and difficulty indicators
* Simple navigation between recipe list and recipe details

---

## 5. Welcome Page

A custom welcome page was developed that displays:

* A list of all recipes
* Cooking time for each recipe
* Dynamically calculated difficulty
* Recipe images

Screenshot saved as:

```
welcome.jpg
```

---

## 6. Recipes List Page

A dedicated recipes overview page was created using a **class-based ListView**:

* All recipes are displayed dynamically from the database
* Each recipe name is clickable
* Images and difficulty are shown

Screenshot saved as:

```
recipes-overview.jpg
```

---

## 7. Recipe Detail Pages

A **DetailView** was implemented to display individual recipe details:

* Name
* Description
* Cooking time
* Difficulty (calculated)
* Image
* Navigation link back to the recipe list

Screenshots saved as:

```
recipe1.jpg
recipe2.jpg
```

---

## 8. Tests

Basic functionality was manually verified:

* Recipe list page loads correctly
* Clicking a recipe opens the correct detail page
* Images load properly from the media folder
* Difficulty calculation updates correctly when cooking time changes

---

## 9. GitHub Upload

The following were uploaded to GitHub:

* Folder:

  ```
  achievement-2/Exercise-2.5/
  ```

  * `Task-2.5.md`
  * `Screenshots/`

* Updated source code pushed to the existing **recipe-app** repository

---

## 10. Summary

In Exercise 2.5, the Recipe application was extended to:

* Support media uploads
* Display database records using class-based views
* Dynamically calculate and present business logic
* Connect list and detail pages using Django URLs
* Present a clean, functional frontend

All task requirements were completed successfully, and the application runs without errors.
