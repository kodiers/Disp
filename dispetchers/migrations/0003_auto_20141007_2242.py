# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dispetchers', '0002_auto_20141007_2234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'},
        ),
        migrations.AlterField(
            model_name='order',
            name='PrefferedTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 7, 22, 42, 8, 895171)),
        ),
    ]
