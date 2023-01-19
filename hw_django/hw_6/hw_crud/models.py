from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=60, unique=True)
    description = models.TextField(null=True, blank=True)


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField(default=18)


class Stock(models.Model):
    address = models.CharField(max_length=200, unique=True)


