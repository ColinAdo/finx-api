from django.contrib import admin
from django.contrib.admin import ModelAdmin


from .models import Comment

# Comment admin
class CommentAdmin(ModelAdmin):
    list_display = [
        'owner',
        'post',
        'comment',
        'created_at'
    ]


admin.site.register(Comment, CommentAdmin)
