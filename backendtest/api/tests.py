from django.test import TestCase
from .models import Recipe, Ingredient, Step
from django.contrib.auth.models import User
# Create your tests here.
class ModelTestCase(TestCase):

    def test_create_recipe_with_ingredients_and_steps(self):

        # gerneric user
        self.user = User()
        self.user.save()
        
        # test recipe
        self.recipe = Recipe(name="test recipe", user=self.user)

        old_count = Recipe.objects.count()
        self.recipe.save()
        new_count = Recipe.objects.count()
        self.assertNotEqual(old_count, new_count)

        # test ingredient
        self.ingredient = Ingredient(text="test ingredient", recipe=self.recipe)

        old_count = Ingredient.objects.count()
        self.ingredient.save()
        new_count = Ingredient.objects.count()
        self.assertNotEqual(old_count, new_count)

        # test step
        self.step = Step(step_text="test step", recipe=self.recipe)

        old_count = Step.objects.count()
        self.step.save()
        new_count = Step.objects.count()
        self.assertNotEqual(old_count, new_count)