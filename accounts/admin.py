from django.contrib.auth.admin import UserAdmin
from django.utils.html import mark_safe
from django.contrib import admin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Custom user admin
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = [
        'username',
        'email',
        'display_file',
        'is_active',
        'is_superuser',
    ]

    def display_file(self, obj):
        return mark_safe('<a href="{}"> <img src="{}" width="30" height="30" style="border-radius: 50%;" /> </a>'.format(obj.profile_picture.url, obj.profile_picture.url))
        
    display_file.short_description = 'File'

admin.site.register(CustomUser, CustomUserAdmin)
