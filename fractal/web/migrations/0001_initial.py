# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '__first__'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('order', models.IntegerField(default=0)),
                ('rename', models.TextField(blank=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('menu', models.ForeignKey(related_name='items', to='web.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to=b'', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PageCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('parent', models.ForeignKey(related_name='sub_sections', blank=True, to='web.PageCategory', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='category',
            field=models.ForeignKey(related_name='pages', blank=True, to='web.PageCategory', null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='group',
            field=models.ForeignKey(blank=True, to='organisation.Group', null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='owner',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
        ),
    ]
