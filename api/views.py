from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import AnimalSerializer, ProductSerializer
from main.models import Animal, Product


# Create your views here.

@api_view(['GET', 'POST'])
def get_animal_list(request):
    animals = Animal.objects.all()
    serializer = AnimalSerializer(animals, many=True)
    print(serializer)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def get_product_list(request):
    products = Product.objects.filter(name__icontains='triol')
    serializer2 = ProductSerializer(products, many=True)
    print(serializer2)
    return Response(serializer2.data)