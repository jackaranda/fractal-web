# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroupCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroupMembership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=20, choices=[(b'chair', b'chair'), (b'member', b'member'), (b'observer', b'observer')])),
                ('group', models.ForeignKey(to='organisation.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=100)),
                ('acroynm', models.CharField(max_length=15)),
                ('description', models.TextField(blank=True)),
                ('logo', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'/data/work/projects/research/fractal/website/fractal-web/fractal/uploads/organisation/logos'), upload_to=b'', blank=True)),
                ('url', models.URLField(blank=True)),
                ('order', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(blank=True, max_length=10, choices=[(b'Mr', b'Mr'), (b'Dr', b'Dr'), (b'Mrs', b'Mrs'), (b'Miss', b'Miss')])),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('url', models.URLField(blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('bio', models.TextField(blank=True)),
                ('photo', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'/data/work/projects/research/fractal/website/fractal-web/fractal/uploads/organisation/photos'), upload_to=b'', blank=True)),
                ('order', models.IntegerField(default=0)),
                ('groups', models.ManyToManyField(to='organisation.Group', through='organisation.GroupMembership')),
                ('organisation', models.ForeignKey(related_name='people', blank=True, to='organisation.Organisation', null=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='organisation',
            name='contact',
            field=models.ForeignKey(related_name='contact_for', blank=True, to='organisation.Person', null=True),
        ),
        migrations.AddField(
            model_name='groupmembership',
            name='person',
            field=models.ForeignKey(to='organisation.Person'),
        ),
        migrations.AddField(
            model_name='group',
            name='category',
            field=models.ForeignKey(related_name='groups', to='organisation.GroupCategory'),
        ),
    ]
