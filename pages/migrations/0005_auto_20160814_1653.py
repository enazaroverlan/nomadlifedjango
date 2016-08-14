# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20160814_1644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagetranslation',
            old_name='translationName',
            new_name='translation',
        ),
    ]
