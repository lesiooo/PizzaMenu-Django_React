from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', PizzaListCreateView.as_view(), name='list-create-pizza'),
    url(r'^(?P<pizza_id>[-\w]+)/$', PizzaRetriveUpdateDeleteView.as_view(), name='retrive-update-destroy-pizza')
    ]