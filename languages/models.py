# coding=utf-8
from django.db import models


# Create your models here.


class Language(models.Model):
    class Meta:
        verbose_name_plural = 'Языки'
        verbose_name = 'Языки'

    name = models.CharField(max_length=255)
    shortName = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
