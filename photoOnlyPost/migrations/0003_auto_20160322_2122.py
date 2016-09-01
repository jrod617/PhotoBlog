# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import photoOnlyPost.models


class Migration(migrations.Migration):

    dependencies = [
        ('photoOnlyPost', '0002_auto_20160320_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='photopost',
            name='fullPhoto',
            field=models.ImageField(default=b'', upload_to=photoOnlyPost.models.full_photo_file_name, blank=True),
        ),
        migrations.AddField(
            model_name='photopost',
            name='thumbnailPhoto',
            field=models.ImageField(default=b'', upload_to=photoOnlyPost.models.thumb_photo_file_name, blank=True),
        ),
    ]
