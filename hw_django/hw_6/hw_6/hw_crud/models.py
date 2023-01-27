from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=60, unique=True, default='good item')
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.title


class Person(models.Model):
    name = models.CharField(max_length=20, default='johann')
    age = models.PositiveIntegerField(default=18)

    def __str__(self):
        return self.name


class Stock(models.Model):
    address = models.CharField(max_length=200, unique=True, default='moscow')
    head = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.address
