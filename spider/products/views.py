from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters

from spider.products import models, serializers, filters


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = models.Company.objects.filter(is_active=True)
    serializer_class = serializers.CompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.filter(is_active=True)
    serializer_class = serializers.ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = filters.ProductFilter
    filterset_fields = ['title', 'category', 'company']
