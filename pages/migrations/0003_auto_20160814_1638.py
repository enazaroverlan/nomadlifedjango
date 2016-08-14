# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_pagetranslation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u044b', 'verbose_name_plural': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u044b'},
        ),
        migrations.AlterModelOptions(
            name='pagetranslation',
            options={'verbose_name': '\u041f\u0435\u0440\u0435\u0432\u043e\u0434 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b', 'verbose_name_plural': '\u041f\u0435\u0440\u0435\u0432\u043e\u0434\u044b'},
        ),
    ]
