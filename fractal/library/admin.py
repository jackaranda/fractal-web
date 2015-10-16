from django.contrib import admin
from library.models import Source, Publication, Author


admin.site.register(Source)
admin.site.register(Publication)
admin.site.register(Author)