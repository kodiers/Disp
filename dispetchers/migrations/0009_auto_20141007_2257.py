# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dispetchers', '0008_auto_20141007_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='PrefferedTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 7, 22, 57, 15, 50172)),
        ),
    ]
