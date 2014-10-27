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
                ('CategoryName', models.CharField(max_length=30, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f \xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb8')),
            ],
            options={
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('OfferName', models.CharField(max_length=150, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x83\xd1\x81\xd0\xbb\xd1\x83\xd0\xb3\xd0\xb8')),
                ('OfferPrice', models.FloatField(verbose_name=b'\xd0\xa1\xd1\x82\xd0\xbe\xd0\xb8\xd0\xbc\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c')),
                ('Duration', models.FloatField(default=1.0, null=True, verbose_name=b'\xd0\x91\xd0\xb0\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x8f \xd0\xb4\xd0\xbb\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c')),
                ('OfferCategory', models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', to='dispetchers.Category')),
            ],
            options={
                'verbose_name_plural': '\u0423\u0441\u043b\u0443\u0433\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ClientName', models.CharField(max_length=150, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f \xd0\xba\xd0\xbb\xd0\xb8\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0')),
                ('ClientAddress', models.CharField(max_length=200, verbose_name=b'\xd0\x90\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81 \xd0\xba\xd0\xbb\xd0\xb8\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0')),
                ('PrefferedTime', models.DateTimeField(default=datetime.datetime(2014, 10, 27, 22, 31, 41, 486675), verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb4\xd0\xbf\xd0\xbe\xd1\x87\xd0\xb5\xd1\x82\xd0\xb0\xd0\xb5\xd0\xbc\xd0\xbe\xd0\xb5 \xd0\xb2\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f')),
                ('CreateTime', models.DateTimeField(default=datetime.datetime(2014, 10, 27, 22, 31, 41, 486718), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('FactTime', models.DateTimeField(null=True, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd0\xba\xd0\xbe\xd0\xb5 \xd0\xb2\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f', blank=True)),
                ('PlanTotalSumm', models.FloatField(null=True, verbose_name=b'\xd0\x9f\xd0\xbb\xd0\xb0\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x8f \xd1\x81\xd1\x82\xd0\xbe\xd0\xb8\xd0\xbc\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c')),
                ('FactTotalSumm', models.FloatField(null=True, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd0\xba\xd0\xb0\xd1\x8f \xd1\x81\xd1\x82\xd0\xbe\xd0\xb8\xd0\xbc\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c')),
                ('Status', models.CharField(default=b'New', max_length=15, verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x82\xd1\x83\xd1\x81', choices=[(b'NEW', b'\xd0\x9d\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x8f'), (b'SET', b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xbd\xd0\xb0\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb0'), (b'INPROGRESS', b'\xd0\x92 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb5'), (b'COMPLETED', b'\xd0\x92\xd1\x8b\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb0')])),
            ],
            options={
                'get_latest_by': 'CreateTime',
                'verbose_name_plural': '\u0417\u0430\u044f\u0432\u043a\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderOfferDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FactWorkedHours', models.TimeField(null=True, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd0\xba\xd0\xb8\xd0\xb5 \xd1\x87\xd0\xb0\xd1\x81\xd1\x8b', blank=True)),
                ('Comments', models.TextField(null=True, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb8', blank=True)),
                ('OfferName', models.ForeignKey(verbose_name=b'\xd0\xa3\xd1\x81\xd0\xbb\xd1\x83\xd0\xb3\xd0\xb0', to='dispetchers.Offer', null=True)),
                ('OrderName', models.ForeignKey(to='dispetchers.Order', null=True)),
            ],
            options={
                'verbose_name_plural': '\u0414\u0435\u0442\u0430\u043b\u0438 \u0437\u0430\u044f\u0432\u043a\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FirstName', models.CharField(max_length=30, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f')),
                ('LastName', models.CharField(max_length=50, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f')),
                ('IsChief', models.BooleanField(default=False, verbose_name=b'\xd0\x91\xd1\x80\xd0\xb8\xd0\xb3\xd0\xb0\xd0\xb4\xd0\xb8\xd1\x80')),
                ('Orders', models.ManyToManyField(to='dispetchers.Order', null=True, verbose_name=b'\xd0\x97\xd0\xb0\xd1\x8f\xd0\xb2\xd0\xba\xd0\xb8', blank=True)),
                ('WorkerCategory', models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', to='dispetchers.Category')),
            ],
            options={
                'verbose_name_plural': '\u0420\u0430\u0431\u043e\u0447\u0438\u0435',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkerHours',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('busyStartTime', models.DateTimeField(null=True)),
                ('busyEndTime', models.DateTimeField(null=True)),
                ('worker', models.ForeignKey(to='dispetchers.Worker')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='orderofferdetail',
            name='Worker',
            field=models.ForeignKey(verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x87\xd0\xb8\xd0\xb9', to='dispetchers.Worker', null=True),
            preserve_default=True,
        ),
    ]
