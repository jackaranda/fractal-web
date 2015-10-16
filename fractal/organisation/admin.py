from django.contrib import admin
from organisation.models import Organisation, GroupCategory, Group, Person, GroupMembership

class OrganisationAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}


admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(GroupCategory)
admin.site.register(Group)
admin.site.register(Person)

