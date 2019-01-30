from django.db import models
from rest_framework.reverse import reverse


class Pizza(models.Model):
    pizza_id = models.UUIDField(primary_key=True ,editable=False, unique=True)
    name = models.CharField(max_length=30, blank=False)
    price = models.DecimalField(max_digits=5, blank=False, decimal_places=2)
    crust = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.name + ' ' + self.crust

    def get_absolute_url(self, request=None):
        return reverse('retrive-update-destroy-pizza', kwargs={'pizza_id': self.pizza_id}, request=request)
