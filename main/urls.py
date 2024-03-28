from django.urls import path

from .views import get_page, get_result_search, get_basket

urlpatterns = [
     path('', get_page),
     path('result/', get_result_search, name='result'),
     path('basket/', get_basket, name='basket')
]
