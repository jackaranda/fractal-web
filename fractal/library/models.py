from django.db import models
from django.conf import settings


class Source(models.Model):

	SOURCE_TYPE = (('Academic Journal', 'journal'), ('Non-governmental Org.', 'NGO'), ('Development Agency', 'agency'), ('Institute', 'institute'))

	sourcetype = models.CharField(max_length=20, choices=SOURCE_TYPE, blank=True)
	name = models.CharField(max_length=200)
	url = models.URLField()


class Publication(models.Model):

	PUB_TYPE = (('Journal Article', 'article'), ('White Paper', 'whitepaper'), ('Other', 'other'))

	pubtype = models.CharField(max_length=20, choices=PUB_TYPE)

	doi = models.CharField(max_length=200, blank=True)
	uri = models.URLField(max_length=500, blank=True)

	title = models.CharField(max_length=500)
	abstract = models.TextField(blank=True)
	synopsis = models.TextField(blank=True)

	source = models.ForeignKey('Source', blank=True, null=True)
	volume = models.IntegerField(blank=True)
	issue = models.IntegerField(blank=True)
	startpage = models.IntegerField(blank=True)
	endpage = models.IntegerField(blank=True)
	date = models.DateField(blank=True, null=True)
	authors = models.ManyToManyField('Author', through='PublicationAuthors')

	contents = models.FileField(blank=True)

	def __unicode__(self):
		return title


class Author(models.Model):

	firstname = models.CharField(max_length=40)
	lastname = models.CharField(max_length=40)
	affiliation = models.CharField(max_length=200)


class PublicationAuthors(models.Model):

	publication = models.ForeignKey('Publication')
	author = models.ForeignKey('Author')
	order = models.IntegerField()




