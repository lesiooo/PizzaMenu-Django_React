import uuid
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Ingredient, Ingredient2Pizza
from pizza.models import Pizza

class IngredientApiTestCase(APITestCase):
    def setUp(self):
        test_ingredient = Ingredient.objects.create(ingredient_id =uuid.uuid4() ,name='test_ingredient', cost='2.50')
        test_ingredient2 = Ingredient.objects.create(ingredient_id =uuid.uuid4() ,name='test_unused_ingredient', cost='2.50')
        pizza = Pizza.objects.create(pizza_id=uuid.uuid4(), name="test_pizza", price='2.50', crust='thin')
        ingredient2pizza = Ingredient2Pizza.objects.create(ingredient2pizza=test_ingredient, pizza2ingredient=pizza)

    def test_get_list_ingredients(self):
        url = reverse('list-create-ingredient')
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_ingredient(self):
        ingredient = Ingredient.objects.first()
        url = ingredient.get_absolute_url()
        data = {}
        response = self.client.get(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_create_ingredient(self):
        data = {"name": "test ingr", "cost": "7.50"}
        url = reverse('list-create-ingredient')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_create_ingredient_not_unique_name(self):
        data = {"name": "test_ingredient", "cost": "7.50"}
        url = reverse('list-create-ingredient')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_create_ingredient_with_unique_name(self):
        ingredient = Ingredient.objects.get(name='test_ingredient')
        data = {"name": "test_2", "cost": "7.50"}
        url = ingredient.get_absolute_url()

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_create_ingredient_not_unique_name(self):
        ingredient = Ingredient.objects.get(name='test_ingredient')
        data = {"name": "test_unused_ingredient", "cost": "7.50"}
        url = ingredient.get_absolute_url()

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_used_ingredient(self):
        ingredient = Ingredient.objects.get(name='test_ingredient')
        url = ingredient.get_absolute_url()

        response = self.client.delete(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_304_NOT_MODIFIED)

    def test_delete_unused_ingredient(self):
        ingredient = Ingredient.objects.get(name='test_unused_ingredient')
        url = ingredient.get_absolute_url()

        response = self.client.delete(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class Ingredient2PizzaTestCase(APITestCase):

    def setUp(self):
        test_ingredient2 = Ingredient.objects.create(ingredient_id=uuid.uuid4(), name='test_ingredient',
                                                     cost='2.50')

    def test_add_ingredient_to_pizza(self):
        data = {'name': 'Test pizza', 'price': '23.50', 'crust': 'thin'}
        url = reverse('list-create-pizza')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        ingredient = Ingredient.objects.first()
        pizza = Pizza.objects.first()
        data = {'ingredient2pizza': ingredient.ingredient_id, 'pizza2ingredient': pizza.pizza_id}
        url = reverse('list-create-ingredient2pizza')

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ingredient2Pizza.objects.count(), 3)

    def test_delete_ingredient_from_pizza(self):
        data = {'name': 'Test pizza', 'price': '23.50', 'crust': 'thin'}
        url = reverse('list-create-pizza')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        ingredient = Ingredient.objects.get(name='test_ingredient')
        pizza = Pizza.objects.first()
        data = {'ingredient2pizza': ingredient.ingredient_id, 'pizza2ingredient': pizza.pizza_id}
        url = reverse('list-create-ingredient2pizza')

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ingredient2Pizza.objects.count(), 3)

        url = reverse('retrive-destroy-ingredient2pizza', kwargs={'pizza_id': pizza.pizza_id, 'ingredient_id': ingredient.ingredient_id})
        response = self.client.delete(url, data={}, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


