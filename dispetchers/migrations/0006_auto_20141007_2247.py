# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dispetchers', '0005_auto_20141007_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CategoryName',
            field=models.CharField(max_length=30, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f \xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='OfferName',
            field=models.CharField(max_length=150, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x83\xd1\x81\xd0\xbb\xd1\x83\xd0\xb3\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='order',
            name='PrefferedTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 7, 22, 47, 53, 815423)),
        ),
    ]
