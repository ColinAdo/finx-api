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
        return mark_safe('<a href="{}"> <img src="{}" width="30" height="30" style="border-radius: 50%;" /> </a>'.format(obj.profile_picture, obj.profile_picture))
        
    display_file.short_description = 'File'

    fieldsets = UserAdmin.fieldsets + ((None, {"fields": (
        "profile_picture",
        "profession",
        "header",
        "github",
        "instagram",
        "linkedin",
        "x",
        )}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": (
        "profile_picture",
        "profession",
        "header",
        "github",
        "instagram",
        "linkedin",
        "x",
        )}),)

admin.site.register(CustomUser, CustomUserAdmin)
