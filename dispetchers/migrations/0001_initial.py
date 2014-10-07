# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CategoryName', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('OfferName', models.CharField(max_length=150)),
                ('OfferPrice', models.FloatField()),
                ('OfferCategory', models.ForeignKey(to='dispetchers.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ClientName', models.CharField(max_length=150)),
                ('ClientAddress', models.CharField(max_length=200)),
                ('PrefferedTime', models.DateTimeField(default=datetime.datetime(2014, 10, 7, 22, 27, 40, 944482))),
                ('FactTime', models.DateTimeField(null=True, blank=True)),
                ('PlanTotalSumm', models.FloatField()),
                ('FactTotalSumm', models.FloatField()),
                ('Status', models.CharField(default=b'New', max_length=15, choices=[(b'NEW', b'\xd0\x9d\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x8f'), (b'SET', b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xbd\xd0\xb0\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb0'), (b'INPROGRESS', b'\xd0\x92 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb5'), (b'COMPLETED', b'\xd0\x92\xd1\x8b\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb0')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderOfferDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FactWorkedHours', models.TimeField(null=True, blank=True)),
                ('Comments', models.TextField()),
                ('OfferName', models.ForeignKey(to='dispetchers.Offer')),
                ('OrderName', models.ForeignKey(to='dispetchers.Order')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=50)),
                ('IsBusy', models.BooleanField(default=False)),
                ('IsChief', models.BooleanField(default=False)),
                ('WorkerCategory', models.ForeignKey(to='dispetchers.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='orderofferdetail',
            name='Worker',
            field=models.ForeignKey(to='dispetchers.Worker'),
            preserve_default=True,
        ),
    ]
