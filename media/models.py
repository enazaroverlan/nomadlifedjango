# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Media(models.Model):
    class Meta:
        verbose_name_plural = 'Медиа'
        verbose_name = 'Медиа'

    title = models.CharField(max_length=255)
    file = models.ImageField(upload_to='')
    timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.title)