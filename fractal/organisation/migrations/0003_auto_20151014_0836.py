# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0002_auto_20151014_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='contact',
            field=models.ForeignKey(related_name='contact_for', blank=True, to='organisation.Person', null=True),
        ),
    ]
