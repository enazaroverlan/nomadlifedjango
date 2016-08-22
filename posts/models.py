# coding=utf-8
from __future__ import unicode_literals
from redactor.fields import RedactorField
from django.db import models


# Create your models here.


class Post(models.Model):
    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новости'
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = RedactorField(verbose_name='Контент')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return 'id: ' + str(self.id)


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
        return 'Перевод для поста: ' + str(self.post.title) + ', Язык: ' + str(self.translation.name)
