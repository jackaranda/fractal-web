# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0004_auto_20151014_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='bio',
            field=models.TextField(blank=True),
        ),
    ]
