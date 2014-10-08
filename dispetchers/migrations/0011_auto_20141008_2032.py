# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dispetchers', '0010_auto_20141007_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='Orders',
            field=models.ManyToManyField(to='dispetchers.Order'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='PrefferedTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 8, 20, 32, 8, 763469)),
        ),
    ]
