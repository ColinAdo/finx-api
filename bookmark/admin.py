from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Bookmark

# bookmark admin
class BookmarkAdmin(ModelAdmin):
    list_display = [
        'user',
        'post'
    ]


admin.site.register(Bookmark, BookmarkAdmin)