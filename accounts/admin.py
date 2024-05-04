from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = [
        "username",
        "email",
        "is_active",
        "is_superuser",
    ]


admin.site.register(CustomUser, CustomUserAdmin)
