# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('shortName', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': '\u042f\u0437\u044b\u043a\u0438',
                'verbose_name_plural': '\u042f\u0437\u044b\u043a\u0438',
            },
        ),
    ]
