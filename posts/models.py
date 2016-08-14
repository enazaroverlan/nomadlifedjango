# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Post(models.Model):
    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новости'

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.id


class PostTranslation(models.Model):
    class Meta:
        verbose_name_plural = 'Переводы'
        verbose_name = 'Перевод новости'

    post = models.ForeignKey(Post)
    translation = models.ForeignKey('languages.Language')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()

    def __unicode__(self):
        return 'Перевод для поста: ' + self.post.title + ', Язык: ' + self.translation.name
