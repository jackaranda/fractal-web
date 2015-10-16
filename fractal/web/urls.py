from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^organisations/(?P<slug>.*)/$', views.organisation, name='organisation'),
	url(r'^organisations/$', views.organisation, name='organisation_list'),
	url(r'^people/(?P<fullname>.*)/$', views.people, name='people'),
	url(r'^people/$', views.people, name='people_list'),
	url(r'^(?P<path>.*)/$', views.page, name='page'),
]

