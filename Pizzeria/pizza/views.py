import uuid
from ingredients.models import Ingredient, Ingredient2Pizza
from django.shortcuts import render
from rest_framework import generics, filters
from .models import Pizza
from .serializers import PizzaSerializer
import django_filters.rest_framework

def default_pizza_ingriedients(pizza_id):
    cheese, cheese_status = Ingredient.objects.get_or_create(name='Cheese', defaults={'ingredient_id':uuid.uuid4(), 'cost': '0.0'})
    sauce, sauce_status = Ingredient.objects.get_or_create(name='Sauce', defaults={'ingredient_id':uuid.uuid4(), 'cost': '0.0'})
    pizza = Pizza.objects.get(pizza_id=pizza_id)
    Ingredient2Pizza.objects.create(ingredient2pizza=cheese, pizza2ingredient=pizza)
    Ingredient2Pizza.objects.create(ingredient2pizza=sauce, pizza2ingredient=pizza)
    print(cheese_status, sauce_status)


class PizzaListCreateView(generics.ListCreateAPIView):
    model = Pizza
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name')
    #filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    #filter_fields = ('name')

    def perform_create(self, serializer):
        pizza_id = uuid.uuid4()
        serializer.save(
            pizza_id=pizza_id
        )
        default_pizza_ingriedients(pizza_id)

class PizzaRetriveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pizza_id'
    model = Pizza
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()
