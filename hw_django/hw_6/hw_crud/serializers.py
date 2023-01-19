from rest_framework import serializers
from .models import Product, Stock, Person


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description']


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['address']


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['age', 'name']
