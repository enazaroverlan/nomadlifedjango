# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20160814_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=redactor.fields.RedactorField(verbose_name='\u041a\u043e\u043d\u0442\u0435\u043d\u0442'),
        ),
    ]
