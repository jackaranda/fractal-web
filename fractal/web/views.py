from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import redirect
import logging

# Get an instance of a logger
logger = logging.getLogger('django')

from django.forms import ModelForm

from models import PageCategory, Page
from organisation.models import Organisation, Person


class PageForm(ModelForm):
	class Meta:
		model = Page
		fields = ['title', 'content']

class OrganisationForm(ModelForm):
	class Meta:
		model = Organisation
		fields = ['name', 'url', 'description', 'logo']

class PersonForm(ModelForm):
	class Meta:
		model = Person
		fields = ['firstname', 'lastname', 'email', 'url', 'bio']

def page(request, path):

	parts = path.split('/')

	logging.error(parts)
	user = request.user

	# PageCategory may be None
	PageCategory = None
	
	# Try and find the PageCategory path
	for part in parts[:-2]:
		try:
			PageCategory = PageCategory.objects.get(slug=part)
		except:
			raise Http404("PageCategory does not exist: {}".format(part))

	# Now try to find the page 
	try:
		page = Page.objects.get(slug=parts[-2], category=PageCategory)
	except:
		logging.error(parts)
		raise Http404("Page does not exist: {}".format(parts))


	# See if we are viewing or editing or updating
	if request.method == 'GET':

		if 'edit' in request.GET:
			form = PageForm()
			return render(request, 'web/page-edit.html', {'request':request, 'path': path, 'page':page, 'user':user, 'form':form})
		else:
			return render(request, 'web/page.html', {'path': path, 'page':page, 'user':user})

	elif request.method == 'POST':

		postform = PageForm(request.POST)

		if postform.is_valid():

			page.title = postform.cleaned_data['title']
			page.content = postform.cleaned_data['content']

			page.save()

			return redirect('page', path)

		else:
			raise Http404("Woah, what happened!")



def organisation(request, slug=None):

	if slug:
		try:
			orgs = [Organisation.objects.get(slug=slug)]
		except:
			raise Http404("Organisation {} does not exist".format(slug))
		finally:
			single = True
	else:
		orgs = Organisation.objects.filter().order_by('order')
		single = False

	form = None
	edit = 'edit' in request.GET

	if edit:
		form = OrganisationForm()

	if request.method == 'GET':
		return render(request, 'web/organisation.html', {'organisations':orgs, 'single':single, 'edit':edit, 'form':form})

	elif request.method == 'POST':

		org = orgs[0]
		form = OrganisationForm(request.POST)

		if form.is_valid():
			org.name = form.cleaned_data['name']
			org.url = form.cleaned_data['url']
			org.description = form.cleaned_data['description']
			#org.logo = form.cleaned_data['logo']
			org.save()
			return redirect('web:organisation', slug)

		else:
			logging.error(form.errors)
			return render(request, 'web/organisation.html', {'organisations':orgs, 'single':single, 'edit':edit, 'form':form})



def people(request, fullname=None):

	logging.error(fullname)

	if fullname:
		firstname, lastname = fullname.split('_')
		try:
			people = [Person.objects.get(firstname=firstname, lastname=lastname)]
		except:
			raise Http404("Person {} does not exist".format(fullname))
		single = True
	else:
		people = Person.objects.filter().order_by('order')
		single = False

	form = None
	edit = 'edit' in request.GET


	if edit:
		form = PersonForm()

	if request.method == 'GET':
		return render(request, 'web/people.html', {'people':people, 'single':single, 'edit':edit, 'form':form})

	elif request.method == 'POST':

		person = people[0]
		form = PersonForm(request.POST)

		if form.is_valid():
			person.firstname = form.cleaned_data['firstname']
			person.lastname = form.cleaned_data['lastname']
			person.url = form.cleaned_data['url']
			person.email = form.cleaned_data['email']
			person.bio = form.cleaned_data['bio']
			person.save()
			return redirect('web:people', fullname)

		else:
			logging.error(form.errors)
			return render(request, 'web/people.html', {'organisations':orgs, 'single':single, 'edit':edit, 'form':form})
