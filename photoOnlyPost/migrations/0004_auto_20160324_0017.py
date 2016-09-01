# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import photoOnlyPost.models


class Migration(migrations.Migration):

    dependencies = [
        ('photoOnlyPost', '0003_auto_20160322_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='photopost',
            name='autoResizeOnSave',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='photopost',
            name='photo',
            field=models.ImageField(upload_to=photoOnlyPost.models.photo_file_name),
        ),
    ]
