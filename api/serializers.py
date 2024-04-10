from rest_framework import serializers


class AnimalSerializer(serializers.Serializer):
    name = serializers.CharField()
    image = serializers.ImageField()


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()