from django.contrib import admin

from spider.products import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_dispaly = ['description', 'is_active']
    list_filter = ['is_active']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'category', 'company', 'is_active']
    list_filter = ['is_active']
