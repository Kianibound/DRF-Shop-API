from rest_framework import filters
import django_filters
from api.models import Product


class InStockFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(stock__gt=0)


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['iexact', 'icontains'],
            'price': ['exact', 'gt', 'gte', 'lt', 'lte', 'range'],
        }
