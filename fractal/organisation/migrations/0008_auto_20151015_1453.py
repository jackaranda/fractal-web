# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0007_person_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='last_name',
            new_name='lastname',
        ),
    ]
