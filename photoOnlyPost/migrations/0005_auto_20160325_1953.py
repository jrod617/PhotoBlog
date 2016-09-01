# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoOnlyPost', '0004_auto_20160324_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='photopost',
            name='photographer',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='photopost',
            name='producer',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
