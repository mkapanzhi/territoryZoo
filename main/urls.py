from django.urls import path

from orders.views import order_create
from .views import get_page, get_result_search, get_basket, cart_add, cart_remove, animal_add, getFile2

urlpatterns = [
     path('', get_page, name='main'),
     path('result/', get_result_search, name='result'),
     path('basket/', get_basket, name='basket'),
     path('add/<int:product_id>/', cart_add, name='cart_add'),
     path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
     path('orders/', order_create, name='order_create'),
     path('animal_add/', animal_add, name='animal_add'),
     path('get_file2/', getFile2, name='get_file2')
]
