from django.shortcuts import render

# Create your views here.
from .models import Recipe, Step, Ingredient
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.views.generic import View
from rest_framework.views import APIView
import json
from django.forms.models import model_to_dict


def serializeAndHttpFormat(objects):
    return  HttpResponse(serializers.serialize('json', objects), content_type="application/json")

class RecipiesViewDetailed(APIView):
    def get(self, request, **kwargs):
        recipies = []
        if "id" in request.GET:
            recipies = [Recipe.objects.get(id=request.GET["id"])]
        else:
            recipies = Recipe.objects.all()

        out = []
        for r in recipies:
            r = model_to_dict(r, fields=[field.name for field in r._meta.fields])
            r['steps'] = [model_to_dict(s, fields=[field.name for field in s._meta.fields]) for s in Step.objects.filter(recipe=r["id"])]
            r['ingredients'] = [model_to_dict(i, fields=[field.name for field in i._meta.fields]) for i in Ingredient.objects.filter(recipe=r["id"])]
            
            out.append(r)


        out = json.dumps(out)
        print (out)

        return HttpResponse(out, content_type="application/json")


class RecipiesView(APIView):
    def get(self, request, **kwargs):
        if "id" in request.GET:
            return serializeAndHttpFormat([Recipe.objects.get(id=request.GET["id"])])

        if "user_id" in request.GET:
            return serializeAndHttpFormat(Recipe.objects.filter(user_id=request.GET["user_id"]))

        return serializeAndHttpFormat(Recipe.objects.all())

    def post(self, request, **kwargs):
        body = json.loads(request.body)
        new = Recipe(name=body["name"], user=User.objects.get(id=body["user_id"]))
        new.save()

        return serializeAndHttpFormat(Recipe.objects.all())

    def delete(self, request, **kwargs):
        body = json.loads(request.body)
        
        if "id" in body:
            Recipe.objects.get(id=body["id"]).delete()

        return serializeAndHttpFormat(Recipe.objects.all())
    

    def patch(self, request, **kwargs):
        body = json.loads(request.body)
        
        if "id" in body:
            toUpdate = Recipe.objects.get(id=body["id"])

            if "name" in body:
                toUpdate.name = body["name"]
            
            if "user" in body:
                toUpdate.user = User.objects.get(id=body["user"])

            toUpdate.save()

        return serializeAndHttpFormat(Recipe.objects.all())


class StepsView(APIView):
    def get(self, request, **kwargs):
        if "id" in request.GET:
            return serializeAndHttpFormat([Step.objects.get(id=request.GET["id"])])

        return serializeAndHttpFormat(Step.objects.all())

    def post(self, request, **kwargs):
        body = json.loads(request.body)
        new = Step(step_text=body["step_text"], recipe=Recipe.objects.get(id=body["recipe_id"]))
        new.save()

        return serializeAndHttpFormat(Step.objects.all())

class IngredientsView(APIView):
    def get(self, request, **kwargs):
        if "id" in request.GET:
            return serializeAndHttpFormat([Ingredient.objects.get(id=request.GET["id"])])

        return serializeAndHttpFormat(Ingredient.objects.all())

    def post(self, request, **kwargs):
        body = json.loads(request.body)
        new = Ingredient(text=body["text"], recipe=Recipe.objects.get(id=body["recipe_id"]))
        new.save()

        return serializeAndHttpFormat(Ingredient.objects.all())

    