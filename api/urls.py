from django.urls import path

from api.views import get_animal_list, get_product_list, animal_add, get_author, get_author1

urlpatterns = [
    path('get_animal_list/', get_animal_list),
    path('get_product_list/', get_product_list),
    path('animal_add/', animal_add),
    path('books/', get_author),
    path('books1/', get_author1)
]
