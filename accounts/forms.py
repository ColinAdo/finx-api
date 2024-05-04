from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

# Adding fields to AbstractUser
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            "email",
            )
        
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields
