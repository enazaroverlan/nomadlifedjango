# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20160814_1649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posttranslation',
            old_name='translationName',
            new_name='translation',
        ),
    ]
