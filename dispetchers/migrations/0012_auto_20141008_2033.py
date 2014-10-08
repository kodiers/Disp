# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dispetchers', '0011_auto_20141008_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='PrefferedTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 8, 20, 33, 45, 771984)),
        ),
        migrations.AlterField(
            model_name='worker',
            name='Orders',
            field=models.ManyToManyField(to=b'dispetchers.Order', verbose_name=b'\xd0\x97\xd0\xb0\xd1\x8f\xd0\xb2\xd0\xba\xd0\xb8'),
        ),
    ]
