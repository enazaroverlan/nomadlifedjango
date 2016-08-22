# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Page(models.Model):
    class Meta:
        verbose_name_plural = 'Страницы'
        verbose_name = 'Страницы'

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    isArticle = models.BooleanField(default=False)
    article = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return str(self.title)


class PageTranslation(models.Model):
    class Meta:
        verbose_name_plural = 'Переводы'
        verbose_name = 'Перевод страницы'

    page = models.ForeignKey(Page)
    translation = models.ForeignKey('languages.Language')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    article = models.TextField()

    def __unicode__(self):
        return 'Перевод для страницы: ' + self.page.title + ', Язык: ' + self.translation.name