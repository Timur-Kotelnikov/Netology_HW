from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(default="nice item")


class Stock(models.Model):
    address = models.CharField(max_length=200, unique=True, default="Moscow")
    products = models.ManyToManyField(
        to=Product,
        through='StockProduct',
        related_name='stocks',
    )


class StockProduct(models.Model):
    stock = models.ForeignKey(
        to=Stock,
        on_delete=models.CASCADE,
        related_name='positions',
    )
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='positions',
    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
