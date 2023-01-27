from rest_framework import serializers
from .models import Product, Stock, Person


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):
    product = ProductSerializer

    class Meta:
        model = Stock
        fields = ['address', 'head', 'product']