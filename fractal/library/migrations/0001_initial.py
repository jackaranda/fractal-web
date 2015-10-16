# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('affiliation', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pubtype', models.CharField(max_length=20, choices=[(b'Journal Article', b'article'), (b'White Paper', b'whitepaper'), (b'Other', b'other')])),
                ('doi', models.CharField(max_length=200, blank=True)),
                ('uri', models.URLField(max_length=500, blank=True)),
                ('title', models.CharField(max_length=500)),
                ('abstract', models.TextField(blank=True)),
                ('synopsis', models.TextField(blank=True)),
                ('volume', models.IntegerField(blank=True)),
                ('issue', models.IntegerField(blank=True)),
                ('startpage', models.IntegerField(blank=True)),
                ('endpage', models.IntegerField(blank=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('contents', models.FileField(upload_to=b'', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PublicationAuthors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField()),
                ('author', models.ForeignKey(to='library.Author')),
                ('publication', models.ForeignKey(to='library.Publication')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sourcetype', models.CharField(blank=True, max_length=20, choices=[(b'Academic Journal', b'journal'), (b'Non-governmental Org.', b'NGO'), (b'Development Agency', b'agency'), (b'Institute', b'institute')])),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='publication',
            name='authors',
            field=models.ManyToManyField(to='library.Author', through='library.PublicationAuthors'),
        ),
        migrations.AddField(
            model_name='publication',
            name='source',
            field=models.ForeignKey(blank=True, to='library.Source', null=True),
        ),
    ]
