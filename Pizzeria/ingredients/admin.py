from django.contrib import admin
from .models import Ingredient, Ingredient2Pizza

class IngredientAdmin(admin.ModelAdmin):
    list_display = ['ingredient_id', 'name', 'cost']
admin.site.register(Ingredient, IngredientAdmin)


class Ingredient2PizzaAdmin(admin.ModelAdmin):
    list_display = ['ingredient2pizza', 'pizza2ingredient']
    fields = ['ingredient2pizza', 'pizza2ingredient']
admin.site.register(Ingredient2Pizza,Ingredient2PizzaAdmin)

# Register your models here.
