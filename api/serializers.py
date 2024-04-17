from rest_framework import serializers

from main.models import Product, Animal


class AnimalSerializer(serializers.Serializer):
    name = serializers.CharField()
    image = serializers.ImageField()


class ProductSerializer(serializers.ModelSerializer):
    # name = serializers.CharField()
    class Meta:
        model = Product
        fields = ['id', 'name', 'image_preview']


class AnimalSerializer(serializers.ModelSerializer):
    # name = serializers.CharField()
    class Meta:
        model = Animal
        fields = "__all__"


class ShopSerializer(serializers.Serializer):
    name = serializers.CharField()


class BooksSerializer(serializers.Serializer):
    name = serializers.CharField()
    shop_set = ShopSerializer(many=True)


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField()
    books_set = BooksSerializer(many=True)


class AuthorSerializer1(serializers.Serializer):
    name = serializers.CharField()


class BooksSerializer1(serializers.Serializer):
    name = serializers.CharField()
    author = AuthorSerializer1(many=True)


class ShopSerializer1(serializers.Serializer):
    name = serializers.CharField()
    book = BooksSerializer1()
