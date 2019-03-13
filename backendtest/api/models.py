from django.db import models
from django.conf import settings

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Step(models.Model):
    step_text = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

class Ingredient(models.Model):
    text = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

