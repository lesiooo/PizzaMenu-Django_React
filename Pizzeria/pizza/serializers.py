from rest_framework import serializers
from rest_framework import validators

from .models import Pizza


class PizzaSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    name = serializers.CharField(max_length=20,
                                 validators=[validators.UniqueValidator(
                                     queryset=Pizza.objects.all(),
                                     message='Powtórzona nazwa składnika.'
                                 )])

    class Meta:
        model = Pizza
        fields = [
            'url',
            'pizza_id',
            'name',
            'price',
            'crust'
        ]

    def get_url(self, obj):
        request = self.context.get('request')
        return obj.get_absolute_url(request=request)