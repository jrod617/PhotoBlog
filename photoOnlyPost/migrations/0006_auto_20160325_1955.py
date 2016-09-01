# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoOnlyPost', '0005_auto_20160325_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photopost',
            name='description',
            field=models.CharField(default=b'', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='photopost',
            name='producer',
            field=models.CharField(default=b'', max_length=200, blank=True),
        ),
    ]
