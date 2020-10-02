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
