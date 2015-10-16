# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0006_person_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
