from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.utils.html import mark_safe

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = [
        "username",
        "email",
        "display_image",
        "is_active",
        "is_superuser",
    ]

    fieldsets = UserAdmin.fieldsets + ((None, { "fields": (
        "header",
        "profile_picture",
        "github", 
        "instagram",
        "x",
        "linkedin",
        "followers",
    )}),)

    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": (
        "header",
        "profile_picture",
        "github",
        "instagram",
        "x",
        "linkedin",
        "followers",
    )}),)

    def display_image(self, obj):
        return mark_safe('<a href="{}"> <img src="{}" width="30" height="30" style="border-radius: 50%;" /> </a>'.format(obj.profile_picture.url, obj.profile_picture.url))
    display_image.short_description = 'Image'


admin.site.register(CustomUser, CustomUserAdmin)
