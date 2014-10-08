# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dispetchers', '0012_auto_20141008_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='CreateTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 8, 20, 48, 10, 868711)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='PrefferedTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 8, 20, 48, 10, 868676)),
        ),
    ]
