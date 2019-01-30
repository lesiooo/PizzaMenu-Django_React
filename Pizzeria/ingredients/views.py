import uuid
from rest_framework import generics, permissions, mixins
from rest_framework import status
from rest_framework.response import Response

from pizza.models import Pizza
from .models import Ingredient, Ingredient2Pizza
from .serializers import IngredientSerializer, Ingredient2PizzaSerializer


class IngredientsListCreateView(generics.ListCreateAPIView):
    model = Ingredient
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(
            ingredient_id = uuid.uuid4()
        )

class IngredientRetriveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'ingredient_id'
    model = Ingredient
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()

    permission_classes = [permissions.AllowAny]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        count_using_ingredients = Ingredient2Pizza.objects.filter(ingredient2pizza=instance.ingredient_id).count()
        print(count_using_ingredients)
        if count_using_ingredients == 0:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_304_NOT_MODIFIED)


class Ingredient2PizzaCreateView(generics.ListCreateAPIView):
    model = Ingredient2Pizza
    serializer_class = Ingredient2PizzaSerializer
    queryset = Ingredient2Pizza.objects.all()

    def perform_create(self, serializer):
        serializer.save(
            pizza2ingredient = Pizza.objects.get(pizza_id=self.request.data['pizza2ingredient']),
            ingredient2pizza = Ingredient.objects.get(ingredient_id=self.request.data['ingredient2pizza'])
        )


class Ingredient2PizzaList(generics.ListAPIView):
    lookup_field = 'pizza_id'
    model = Ingredient2Pizza
    serializer_class = Ingredient2PizzaSerializer
    queryset = Ingredient2Pizza.objects.all()

    def get_queryset(self, *args, **kwargs):

        return self.queryset.filter(pizza2ingredient=self.kwargs['pizza_id'])


class Ingredient2PizzaRetriveDestroyView(generics.RetrieveDestroyAPIView):
    model = Ingredient2Pizza
    serializer_class = Ingredient2PizzaSerializer
    queryset = Ingredient2Pizza.objects.all()

    def get_object(self):
        pizza = Pizza.objects.get(pizza_id=self.kwargs.get('pizza_id'))
        ingredient = Ingredient.objects.get(ingredient_id=self.kwargs.get('ingredient_id'))
        return Ingredient2Pizza.objects.get(pizza2ingredient=pizza, ingredient2pizza=ingredient)






