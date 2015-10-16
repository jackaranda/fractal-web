# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0003_auto_20151014_0836'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organisation',
            old_name='list_order',
            new_name='order',
        ),
        migrations.AlterField(
            model_name='organisation',
            name='logo',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'/data/work/projects/research/fractal/website/django/fractal/uploads/organisation/logos'), upload_to=b'', blank=True),
        ),
    ]
