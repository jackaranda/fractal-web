from django.db import models
from django.conf import settings

from organisation.models import Group

class GeoCategory(models.Model):

	slug = models.SlugField()
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True)

	def __unicode__(self):
		return self.slug

class Place(models.Model):

	slug = models.SlugField()
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	image = models.ImageField(blank=True)

	owner = models.ForeignKey(settings.AUTH_USER_MODEL, default=0)
	category = models.ForeignKey('GeoCategory', related_name='places', blank=True, null=True)
	group = models.ForeignKey(Group, blank=True, null=True)

	created = models.DateTimeField(auto_now=True)
	modified = models.DateTimeField(auto_now_add=True)

