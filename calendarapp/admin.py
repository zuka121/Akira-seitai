from django.contrib import admin
from .models import Event, Request, Notice


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time')

admin.site.register(Event, EventAdmin)



class RequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time', 'treatment_location')
    list_filter = ('treatment_location',)
    search_fields = ('name',)

admin.site.register(Request, RequestAdmin)



class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'content')  # 管理画面で表示するフィールドを指定
    fields = ('title', 'content', 'date')

admin.site.register(Notice, NoticeAdmin)
