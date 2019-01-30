from django.db import models
from rest_framework.reverse import reverse
from pizza.models import Pizza


class Ingredient(models.Model):
    ingredient_id = models.UUIDField(primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=20, unique=True, blank=False)
    cost = models.DecimalField(max_digits=4, decimal_places=2, blank=False)


    def __str__(self):
        return self.name + ' ' + str(self.cost)


    def get_absolute_url(self, request=None):
        return reverse('retrive-update-destroy-ingredient', kwargs={'ingredient_id': self.ingredient_id}, request=request)


class Ingredient2Pizza(models.Model):
    ingredient2pizza = models.ForeignKey(Ingredient, related_name='ingredient_key', on_delete=models.CASCADE)
    pizza2ingredient = models.ForeignKey(Pizza, related_name='pizza_key', on_delete=models.CASCADE)


    def get_pizza_name(self):
        return Pizza.objects.get(pizza_id=self.pizza2ingredient.pizza_id).name

    def get_ingredient_name(self):
        return Ingredient.objects.get(ingredient_id=self.ingredient2pizza.ingredient_id).name
