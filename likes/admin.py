from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import LikePost

# Like admin
class LikeAdmin(ModelAdmin):
    list_display = [
        'user',
        'post'
    ]


admin.site.register(LikePost, LikeAdmin)