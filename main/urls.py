from django.urls import path

from orders.views import order_create
from .views import get_page, get_result_search, get_basket, cart_add, cart_remove

urlpatterns = [
     path('', get_page, name='main'),
     path('result/', get_result_search, name='result'),
     path('basket/', get_basket, name='basket'),
     path('add/<int:product_id>/', cart_add, name='cart_add'),
     path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
     path('orders/', order_create, name='order_create')
]
