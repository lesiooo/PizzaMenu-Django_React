from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Pizza
from ingredients.models import Ingredient2Pizza, Ingredient


class TestPizzaApi(APITestCase):

    def test_get_pizza_list(self):
        url = reverse('list-create-pizza')
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_pizza_and_add_connected_ingredients(self):
        data = {'name': 'Test pizza', 'price': '23.50', 'crust': 'thin'}
        url = reverse('list-create-pizza')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ingredient2Pizza.objects.count(), 2)
        self.assertEqual(Ingredient.objects.count(), 2)

    def test_create_2_simple_pizzas(self):
        data = {'name': 'Test pizza', 'price': '23.50', 'crust': 'thin'}
        url = reverse('list-create-pizza')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ingredient2Pizza.objects.count(), 2)
        self.assertEqual(Ingredient.objects.count(), 2)

        data = {'name': 'Test pizza_2', 'price': '24.50', 'crust': 'thin'}
        url = reverse('list-create-pizza')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ingredient2Pizza.objects.count(), 4)
        self.assertEqual(Ingredient.objects.count(), 2)

    def test_create_2_pizzas_with_the_same_name(self):
        data = {'name': 'Test pizza', 'price': '23.50', 'crust': 'thin'}
        url = reverse('list-create-pizza')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = {'name': 'Test pizza', 'price': '24.50', 'crust': 'thin'}
        url = reverse('list-create-pizza')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_pizza(self):
        data = {'name': 'Test pizza', 'price': '23.50', 'crust': 'thin'}
        url = reverse('list-create-pizza')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ingredient2Pizza.objects.count(), 2)
        self.assertEqual(Ingredient.objects.count(), 2)

        pizza = Pizza.objects.first()
        url = pizza.get_absolute_url()
        self.client.delete(url, {}, format='json')
        self.assertEqual(Ingredient2Pizza.objects.count(), 0)
        self.assertEqual(Ingredient.objects.count(), 2)