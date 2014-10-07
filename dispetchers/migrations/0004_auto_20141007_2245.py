# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dispetchers', '0003_auto_20141007_2242'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='offer',
            options={'verbose_name_plural': '\u0423\u0441\u043b\u0443\u0433\u0438'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': '\u0417\u0430\u044f\u0432\u043a\u0438'},
        ),
        migrations.AlterModelOptions(
            name='worker',
            options={'verbose_name_plural': '\u0420\u0430\u0431\u043e\u0447\u0438\u0435'},
        ),
        migrations.AlterField(
            model_name='order',
            name='PrefferedTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 7, 22, 45, 37, 697746)),
        ),
    ]
