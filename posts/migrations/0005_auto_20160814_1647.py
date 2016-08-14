# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20160814_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posttranslation',
            name='translationName',
            field=models.ForeignKey(to='languages.Language'),
        ),
    ]
