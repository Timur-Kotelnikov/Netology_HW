import django_filters

from .models import Adv


class AdvFilter(django_filters.FilterSet):
    posted_at = django_filters.rest_framework.DateFilter(field_name='posted_at', lookup_expr='date')
    posted_at__gt = django_filters.DateFilter(field_name='posted_at', lookup_expr='date__gt')
    posted_at__lt = django_filters.DateFilter(field_name='posted_at', lookup_expr='date__lt')

    class Meta:
        model = Adv
        fields = ['posted_at']
