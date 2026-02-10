from django.test import TestCase
from .models import Recipe


class RecipeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Recipe.objects.create(
            name="Test Recipe",
            description="Test description",
            cooking_time=25
        )

    def test_recipe_name_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_cooking_time_is_integer(self):
        recipe = Recipe.objects.get(id=1)
        self.assertIsInstance(recipe.cooking_time, int)

    def test_string_representation(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(str(recipe), recipe.name)
