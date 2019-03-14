from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import RecipiesView, RecipiesViewDetailed, IngredientsView, StepsView, UserView

urlpatterns = {
    url(r'^api/recipe$', RecipiesView.as_view(), name="create"),
    url(r'^api/recipe(?P<id>\w+)$', RecipiesView.as_view(), name="create"),
    url(r'^api/recipe(?P<user_id>\w+)$', RecipiesView.as_view(), name="create"),

    url(r'^api/recipe/details(?P<id>\w+|)$', RecipiesViewDetailed.as_view(), name="create"),

    url(r'^api/step$', StepsView.as_view(), name="create"),
    url(r'^api/step(?P<id>\w+|)$', StepsView.as_view(), name="create"),

    url(r'^api/ingredient$', IngredientsView.as_view(), name="create"),
    url(r'^api/ingredient(?P<id>\w+|)$', IngredientsView.as_view(), name="create"),

    url(r'^api/user$', UserView.as_view(), name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)