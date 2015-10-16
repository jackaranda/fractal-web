# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='contact',
            field=models.ForeignKey(related_name='contact_for', to='organisation.Person', null=True),
        ),
    ]
