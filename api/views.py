from _ast import Store

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import Author, Shop
from .serializers import AnimalSerializer, ProductSerializer, AuthorSerializer, ShopSerializer1
from main.models import Animal, Product


# Create your views here.

@api_view(['GET', 'POST'])
def get_animal_list(request):
    animals = Animal.objects.all()
    serializer = AnimalSerializer(animals, many=True)
    print(serializer)
    return Response(serializer.data)


class AnimalListAPIView(ListAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


@api_view(['GET', 'POST'])
def get_product_list(request):
    print(request.query_params)
    products = Product.objects.filter(
        name__icontains=request.query_params.get('search'))
    serializer2 = ProductSerializer(products, many=True)
    print(serializer2)
    return Response(serializer2.data)


@api_view(['POST'])
def animal_add(request):
    new_animal = AnimalSerializer(data=request.data)
    if new_animal.is_valid(raise_exception=True):
        print(new_animal.validated_data)
        animal = Animal(name=new_animal.validated_data.get(
            'name'), image=new_animal.validated_data.get('image'))
        animal.save()
    else:
        print(new_animal.errors)
    return Response()


@api_view(['GET', 'POST'])
def get_author(request):
    author = Author.objects.all()
    author_serializer = AuthorSerializer(author, many=True)
    print(author_serializer)
    return Response(author_serializer.data)


@api_view(['GET', 'POST'])
def get_author1(request):
    store = Shop.objects.all()
    store_serializer = ShopSerializer1(store, many=True)
    print(store)

    return Response(store_serializer.data)
