from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Title'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Company(models.Model):
    description = models.CharField(max_length=250, verbose_name=_('Description'))
    is_active = models.BooleanField(default=False, verbose_name=('Active'))

    def __str__(self):
        return self.description

    class Meta:
        verbose_name=_('Company')
        verbose_name_plural= _('Companies')


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    description = models.CharField(max_length=250, verbose_name=_('Description'))
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name=_('Category'))
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=_('Company'))
    is_active = models.BooleanField(default=False, verbose_name=('Active'))
