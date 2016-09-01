# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import photoOnlyPost.models


class Migration(migrations.Migration):

    dependencies = [
        ('photoOnlyPost', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photopost',
            name='body',
        ),
        migrations.AddField(
            model_name='photopost',
            name='description',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='photopost',
            name='photo',
            field=models.ImageField(default=b'', upload_to=photoOnlyPost.models.photo_file_name, blank=True),
        ),
    ]
