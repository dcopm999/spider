from django.contrib import admin

from spider.products import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_dispaly = ['description', 'is_active']
