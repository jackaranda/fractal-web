from django.db import models
from django.conf import settings

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from organisation.models import Group

class Menu(models.Model):

	name = models.CharField(max_length=30, blank=True)

	def __unicode__(self):
		return 


class MenuItem(models.Model):

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	menu = models.ForeignKey('Menu', related_name="items")
	order = models.IntegerField(default=0)

	rename = models.TextField(blank=True)

	def __unicode__(self):
		return repr(self.content_object)



class PageCategory(models.Model):

	slug = models.SlugField()
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True)

	parent = models.ForeignKey('PageCategory', related_name='sub_sections', blank=True, null=True)

	def __unicode__(self):
		return self.name


class Page(models.Model):

	slug = models.SlugField()
	title = models.CharField(max_length=200)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, default=0)
	group = models.ForeignKey(Group, blank=True, null=True)

	created = models.DateTimeField(auto_now=True)
	modified = models.DateTimeField(auto_now_add=True)

	content = models.TextField(blank=True)
	image = models.ImageField(blank=True)

	category = models.ForeignKey('PageCategory', related_name='pages', blank=True, null=True)

	def __unicode__(self):
		return self.title
