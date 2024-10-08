from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import UserFollow


# User follow admin
class FollowersAdmin(ModelAdmin):
    list_display = [
        'user',
        'follows'
    ]


admin.site.register(UserFollow, FollowersAdmin)
