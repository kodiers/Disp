# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dispetchers', '0013_auto_20141008_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ClientAddress',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x90\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81 \xd0\xba\xd0\xbb\xd0\xb8\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ClientName',
            field=models.CharField(max_length=150, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f \xd0\xba\xd0\xbb\xd0\xb8\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='order',
            name='CreateTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 8, 22, 4, 55, 521373), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='order',
            name='FactTime',
            field=models.DateTimeField(null=True, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd0\xba\xd0\xbe\xd0\xb5 \xd0\xb2\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='FactTotalSumm',
            field=models.FloatField(verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd0\xba\xd0\xb0\xd1\x8f \xd1\x81\xd1\x82\xd0\xbe\xd0\xb8\xd0\xbc\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c'),
        ),
        migrations.AlterField(
            model_name='order',
            name='PlanTotalSumm',
            field=models.FloatField(verbose_name=b'\xd0\x9f\xd0\xbb\xd0\xb0\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x8f \xd1\x81\xd1\x82\xd0\xbe\xd0\xb8\xd0\xbc\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c'),
        ),
        migrations.AlterField(
            model_name='order',
            name='PrefferedTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 8, 22, 4, 55, 521324), verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb4\xd0\xbf\xd0\xbe\xd1\x87\xd0\xb5\xd1\x82\xd0\xb0\xd0\xb5\xd0\xbc\xd0\xbe\xd0\xb5 \xd0\xb2\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='order',
            name='Status',
            field=models.CharField(default=b'New', max_length=15, verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x82\xd1\x83\xd1\x81', choices=[(b'NEW', b'\xd0\x9d\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x8f'), (b'SET', b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xbd\xd0\xb0\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb0'), (b'INPROGRESS', b'\xd0\x92 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb5'), (b'COMPLETED', b'\xd0\x92\xd1\x8b\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb0')]),
        ),
    ]
