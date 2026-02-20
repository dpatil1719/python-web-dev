# Exercise 2.7 — Data Analysis and Visualization in Django

---

## Part 1 — Search Feature Planning

### Search Criteria
Users can search recipes by:
- Recipe name (partial match supported)
- Example searches:
  - "veg" → returns Vegetable Biryani, Vegetable Pasta
  - "pan" → returns Pancakes

### Output Format
Search results are displayed in:
1. A clickable list of recipes
2. A table view using pandas DataFrame
3. Optional chart visualization

---

## Part 2 — Data Analysis

### Bar Chart
- X-axis: Recipe names
- Y-axis: Cooking time (minutes)
- Purpose: Compare cooking times between recipes

### Pie Chart
- Labels: Recipe names
- Values: Cooking times
- Purpose: Show proportion of cooking time per recipe

### Line Chart
- X-axis: Recipe names
- Y-axis: Cooking time
- Purpose: Visual trend of cooking times

---

## Part 3 — Execution Flow

User journey:

1. User lands on homepage
2. User logs in
3. User clicks "Search Recipes"
4. User enters search keyword
5. Recipes are filtered and displayed
6. User selects chart type
7. Visualization appears
8. User clicks recipe for details
9. User logs out

---

## Part 4 — Features Implemented

✔ Login protection on all views  
✔ Partial search using icontains  
✔ Show-all when search box empty  
✔ Clickable results linking to detail page  
✔ Table display using pandas  
✔ Bar / Pie / Line chart using matplotlib  
✔ Unit tests for forms and views  

---

## Part 5 — Testing Outcome

All automated tests passed successfully.

