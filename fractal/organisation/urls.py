from django.conf.urls import url

import views

urlpatterns = [
	url(r'(?P<slug>.*)/$', views.organisation_detail, name='organisation_detail'),
]