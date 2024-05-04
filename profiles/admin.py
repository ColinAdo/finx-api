from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.html import mark_safe

from profiles.models import Profile


class ProfileAdmin(ModelAdmin):
    list_display = [
        "owner", 
        "header",
        "profession", 
        "display_image",
    ]

    def display_image(self, obj):
        return mark_safe('<a href="{}"> <img src="{}" width="30" height="30" style="border-radius: 50%;" /> </a>'.format(obj.profile_picture.url, obj.profile_picture.url))
    display_image.short_description = 'Profile picture'


admin.site.register(Profile, ProfileAdmin)
