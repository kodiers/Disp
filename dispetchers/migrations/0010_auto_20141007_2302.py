# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dispetchers', '0009_auto_20141007_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='OfferCategory',
            field=models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', to='dispetchers.Category'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='OfferPrice',
            field=models.FloatField(verbose_name=b'\xd0\xa1\xd1\x82\xd0\xbe\xd0\xb8\xd0\xbc\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c'),
        ),
        migrations.AlterField(
            model_name='order',
            name='PrefferedTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 7, 23, 2, 10, 972284)),
        ),
        migrations.AlterField(
            model_name='worker',
            name='FirstName',
            field=models.CharField(max_length=30, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='IsBusy',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xbd\xd1\x8f\xd1\x82'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='IsChief',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x91\xd1\x80\xd0\xb8\xd0\xb3\xd0\xb0\xd0\xb4\xd0\xb8\xd1\x80'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='LastName',
            field=models.CharField(max_length=50, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='WorkerCategory',
            field=models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', to='dispetchers.Category'),
        ),
    ]
