# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20160814_1547'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': '\u041d\u043e\u0432\u043e\u0441\u0442\u0438', 'verbose_name_plural': '\u041d\u043e\u0432\u043e\u0441\u0442\u0438'},
        ),
        migrations.AlterModelOptions(
            name='posttranslation',
            options={'verbose_name': '\u041f\u0435\u0440\u0435\u0432\u043e\u0434 \u043d\u043e\u0432\u043e\u0441\u0442\u0438', 'verbose_name_plural': '\u041f\u0435\u0440\u0435\u0432\u043e\u0434\u044b'},
        ),
    ]
