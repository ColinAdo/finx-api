from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.html import mark_safe

from .models import Post

# Post admin 
class PostAdmin(ModelAdmin):
    list_display = [
        'author', 
        'display_file', 
        'caption', 
        'created_at'
    ]

    def display_file(self, obj):
        if obj.fileUrl.endswith('.png') or obj.fileUrl.endswith('.jpg'):
            return mark_safe('<a href="{}"> <img src="{}" width="30" height="30" style="border-radius: 50%;" /> </a>'.format(obj.fileUrl, obj.fileUrl))
        elif obj.fileUrl.endswith('.mp4'):
            return mark_safe('<a href="{}"> <video width="30" height="30" style="border-radius: 50%;" src="{}"></video>  </a>'.format(obj.fileUrl, obj.fileUrl))
        else:
            return 'text post'
    display_file.short_description = 'File'


# Comment admin
class CommentAdmin(ModelAdmin):
    list_display = ["user", "post", "created_at"]

admin.site.register(Post, PostAdmin)
