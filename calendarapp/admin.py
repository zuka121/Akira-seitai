from django.contrib import admin
from .models import Event, Request


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time')

admin.site.register(Event, EventAdmin)



class RequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time', 'treatment_location')
    list_filter = ('treatment_location',)
    search_fields = ('name',)

admin.site.register(Request, RequestAdmin)
