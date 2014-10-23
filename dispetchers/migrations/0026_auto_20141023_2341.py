# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dispetchers', '0025_auto_20141021_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='CreateTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 23, 23, 41, 57, 607020), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='order',
            name='PrefferedTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 23, 23, 41, 57, 606975), verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb4\xd0\xbf\xd0\xbe\xd1\x87\xd0\xb5\xd1\x82\xd0\xb0\xd0\xb5\xd0\xbc\xd0\xbe\xd0\xb5 \xd0\xb2\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='orderofferdetail',
            name='FactWorkedHours',
            field=models.TimeField(null=True, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd0\xba\xd0\xb8\xd0\xb5 \xd1\x87\xd0\xb0\xd1\x81\xd1\x8b', blank=True),
        ),
    ]
