# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0005_person_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='photo',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'/data/work/projects/research/fractal/website/django/fractal/uploads/organisation/photos'), upload_to=b'', blank=True),
        ),
    ]
