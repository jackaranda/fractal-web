from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

logo_storage = FileSystemStorage(location=os.path.join(settings.BASE_DIR, 'uploads/organisation/logos'))
photo_storage = FileSystemStorage(location=os.path.join(settings.BASE_DIR, 'uploads/organisation/photos'))

class Organisation(models.Model):

	slug = models.SlugField()
	name = models.CharField(max_length=100)
	acroynm = models.CharField(max_length=15)
	description = models.TextField(blank=True)
	logo = models.ImageField(storage=logo_storage, blank=True)	
	url = models.URLField(blank=True)
	contact = models.ForeignKey('Person', related_name='contact_for', blank=True, null=True)
	order = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name


class GroupCategory(models.Model):

	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)

	def __unicode__(self):
		return self.title


class Group(models.Model):

	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)

	category = models.ForeignKey(GroupCategory, related_name='groups')

	def __unicode__(self):
		return self.name


class Person(models.Model):

	TITLE_CHOICES = (('Mr', 'Mr'), ('Dr', 'Dr'), ('Mrs','Mrs'), ('Miss', 'Miss'))

	title = models.CharField(max_length=10, choices=TITLE_CHOICES, blank=True)
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	url = models.URLField(blank=True)
	email = models.EmailField(blank=True)
	bio = models.TextField(blank=True)
	photo = models.ImageField(blank=True, storage=photo_storage)

	user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
	order = models.IntegerField(default=0)

	organisation = models.ForeignKey('Organisation', related_name='people', blank=True, null=True)
	groups = models.ManyToManyField('Group', through='GroupMembership')

	def fullname_underscore(self):
		return "{}_{}".format(self.firstname, self.lastname)
		
	def __unicode__(self):
		return "{} {} {}".format(self.title, self.firstname, self.lastname)


class GroupMembership(models.Model):

	CLUSTER_MEMBERSHIP = (('chair', 'chair'), ('member', 'member'), ('observer', 'observer'))
	
	person = models.ForeignKey('Person')
	group = models.ForeignKey('Group')
	role = models.CharField(max_length=20, choices=CLUSTER_MEMBERSHIP)


