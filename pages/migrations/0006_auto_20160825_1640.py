# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20160814_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='article',
        ),
        migrations.AddField(
            model_name='page',
            name='content',
            field=redactor.fields.RedactorField(default=datetime.datetime(2016, 8, 25, 10, 40, 29, 786000, tzinfo=utc), verbose_name='\u041a\u043e\u043d\u0442\u0435\u043d\u0442'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pagetranslation',
            name='article',
            field=redactor.fields.RedactorField(verbose_name='\u041f\u0435\u0440\u0435\u0432\u043e\u0434 \u0441\u0442\u0430\u0442\u044c\u0438'),
        ),
    ]
