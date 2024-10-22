from django.contrib import admin

from .models import Conversation, ConversationMessage

# Registering models
admin.site.register(Conversation)
admin.site.register(ConversationMessage)
