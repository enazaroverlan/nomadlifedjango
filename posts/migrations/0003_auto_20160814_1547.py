# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_posttranslations'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('translationName', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('post', models.ForeignKey(to='posts.Post')),
            ],
        ),
        migrations.RemoveField(
            model_name='posttranslations',
            name='post',
        ),
        migrations.DeleteModel(
            name='PostTranslations',
        ),
    ]
