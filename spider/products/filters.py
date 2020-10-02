from django_filters import rest_framework as filters

from spider.products import models


class ProductFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Product
        fields = ['title', 'company', 'category']
