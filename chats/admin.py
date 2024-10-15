from django.contrib import admin

from .models import Contact, Message, Chat

# Registering models
admin.site.register(Contact)
admin.site.register(Message)
admin.site.register(Chat)
