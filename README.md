# GeniusPlazaBackendTest

Design a REST API using Django REST Framework
Models:
1. Design the User Model with username(unique field), email(unique field), first_name,
last_name,password. (You can use the django inbuilt user model)
2. Design A Step Model with step_text(string field, not null), Many to One relationship with
Recipe
3. Design An Ingredient Model with text(not null, string), Many to One relationship with
Recipe
4. Design A Recipe Model with name(string, not null), Foreign Key to User table(one to one
relationship), One to Many relationship with Step and Ingredient Model

API:
-----
Create API endpoints to create a new recipe, get recipes by particular user, get all the
recipes, update a recipe, delete a particular recipe

- /api/recipe 
  - GET: get all recipies use id=<recipe_id> for a specific, or user_id=<user_id> for all from a user
  - POST: post a new recipe
  - PATCH: update existing one (must include id field)
  - DELETE: Delete existing one (must include id field)
  
- /api/recipe/details
  - GET: get recipies and all steps and ingredients related use id=<recipe_id> for a specific recipe
  
- /api/step
  - GET: all steps id=<step_id> for a specific
  - POST: post a new step
  
- /api/ingredient
  - GET: all steps id=<ingredient_id> for a specific
  - POST: post a new ingredient
