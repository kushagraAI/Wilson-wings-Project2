from django.contrib import admin
from destinations.models import Destination


class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'owner')


admin.site.register(Destination, DestinationAdmin)
