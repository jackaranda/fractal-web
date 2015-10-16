from django.contrib import admin
from web.models import Menu, MenuItem, PageCategory, Page

class MenuAdmin(admin.ModelAdmin):
	pass

class PageAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(PageCategory)
admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem)
admin.site.register(Page, PageAdmin)
