from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.html import mark_safe

from .models import Post

# Post admin 
class PostAdmin(ModelAdmin):
    list_display = ["author", "display_file", "caption", "created_at"]

    def display_file(self, obj):
        if obj.file and obj.get_file_type() == "image":
            return mark_safe('<a href="{}"> <img src="{}" width="30" height="30" style="border-radius: 50%;" /> </a>'.format(obj.file.url, obj.file.url))
        elif obj.file and obj.get_file_type() == "video":
            return mark_safe('<a href="{}"> <video width="30" height="30" style="border-radius: 50%;" src="{}"></video>  </a>'.format(obj.file.url, obj.file.url))
        else:
            return "text post"
    display_file.short_description = 'File'


# Comment admin
class CommentAdmin(ModelAdmin):
    list_display = ["user", "post", "created_at"]

admin.site.register(Post, PostAdmin)
