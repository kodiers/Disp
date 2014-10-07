# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dispetchers', '0004_auto_20141007_2245'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderofferdetail',
            options={'verbose_name_plural': '\u0414\u0435\u0442\u0430\u043b\u0438 \u0437\u0430\u044f\u0432\u043a\u0438'},
        ),
        migrations.AlterField(
            model_name='order',
            name='PrefferedTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 7, 22, 46, 34, 804830)),
        ),
    ]
