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
