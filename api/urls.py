from django.urls import path

from api.views import get_animal_list, get_product_list
from orders.views import order_create


urlpatterns = [
    path('get_animal_list/', get_animal_list),
    path('get_product_list/', get_product_list),

]
