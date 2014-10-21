# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dispetchers', '0024_auto_20141020_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='CreateTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 21, 21, 43, 23, 789637), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='order',
            name='PrefferedTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 21, 21, 43, 23, 789610), verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb4\xd0\xbf\xd0\xbe\xd1\x87\xd0\xb5\xd1\x82\xd0\xb0\xd0\xb5\xd0\xbc\xd0\xbe\xd0\xb5 \xd0\xb2\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='orderofferdetail',
            name='Comments',
            field=models.TextField(null=True, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb8', blank=True),
        ),
        migrations.AlterField(
            model_name='orderofferdetail',
            name='OfferName',
            field=models.ForeignKey(verbose_name=b'\xd0\xa3\xd1\x81\xd0\xbb\xd1\x83\xd0\xb3\xd0\xb0', to='dispetchers.Offer', null=True),
        ),
        migrations.AlterField(
            model_name='orderofferdetail',
            name='Worker',
            field=models.ForeignKey(verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x87\xd0\xb8\xd0\xb9', to='dispetchers.Worker', null=True),
        ),
    ]
