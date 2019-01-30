from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^i/$', IngredientsListCreateView.as_view(), name='list-create-ingredient'),
    url(r'^i/(?P<ingredient_id>[-\w]+)/$', IngredientRetriveUpdateDeleteView.as_view(), name='retrive-update-destroy-ingredient'),

    url(r'^ingredient2pizza/$', Ingredient2PizzaCreateView.as_view(), name='create-ingredient2pizza'),
    url(r'^ingredient2pizza/(?P<pizza_id>[-\w]+)/$', Ingredient2PizzaList.as_view(), name='list-ingredient2pizza'),
    url(r'^ingredient2pizza/(?P<pizza_id>[-\w]+)/(?P<ingredient_id>[-\w]+)/$', Ingredient2PizzaRetriveDestroyView.as_view(),
        name='retrive-destroy-ingredient2pizza'),
    ]
