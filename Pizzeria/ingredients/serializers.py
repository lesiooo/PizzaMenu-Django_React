from rest_framework import serializers, validators
from .models import Ingredient, Ingredient2Pizza
from pizza.models import Pizza


class IngredientSerializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField(read_only=True)
    name = serializers.CharField(max_length=20,
                                 validators=[validators.UniqueValidator(
                                     queryset=Ingredient.objects.all(),
                                     message='Powtórzona nazwa składnika.'
                                 )])
    class Meta:
        model = Ingredient
        fields = [
            'url',
            'ingredient_id',
            'name',
            'cost'
        ]
    def get_url(self, obj):
        request = self.context.get('request')
        return obj.get_absolute_url(request=request)

class Ingredient2PizzaSerializer(serializers.ModelSerializer):

    ingredient_name = serializers.SerializerMethodField(read_only=True)
    pizza_name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Ingredient2Pizza
        fields = [
            'ingredient2pizza',
            'pizza2ingredient',
            'pizza_name',
            'ingredient_name'
        ]

    def get_pizza_name(self, obj):
        return obj.get_pizza_name()

    def get_ingredient_name(self, obj):
        return obj.get_ingredient_name()