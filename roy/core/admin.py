from django.contrib import admin
from . models import Camp, Event, ContactsSaved

#Table to display messages sent by users
class ClientsMessagesAdmin(admin.ModelAdmin):
    list_display = ('subject', 'email', 'first_name', 'last_name', 'message', 'created_date')


admin.site.register(Camp)
admin.site.register(Event)
admin.site.register(ContactsSaved)