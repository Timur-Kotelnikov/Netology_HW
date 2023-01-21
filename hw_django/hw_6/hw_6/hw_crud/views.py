from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from .models import Product, Stock, Person
from .serializers import ProductSerializer, StockSerializer, PersonSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [SearchFilter]
    search_fields = ['address']


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [SearchFilter]
    search_fields = ['age', 'name']

