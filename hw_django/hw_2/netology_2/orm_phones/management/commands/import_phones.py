import csv
from django.core.management.base import BaseCommand
from orm_phones.models import Phone


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('/home/timur/Documents/Python/HW/Netology_hw_nogit/hw_django/hw_2/netology_2/phones.csv', 'r') as f:
            phones = list(csv.DictReader(f, delimiter=';'))

        for phone in phones:
            new = Phone(
                name=phone['name'],
                price=phone['price'],
                image=phone['image'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'],
                slug=phone["name"].replace(" ", "-").lower()
            )
            new.save()
