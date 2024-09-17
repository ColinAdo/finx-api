from django.contrib.auth.models import AbstractUser
from django.db import models

def user_directory_path(instance, filename):
    return 'profile/{0}/{1}'.format(instance.username, filename)

# Custom user model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255)
    header = models.CharField(max_length=200, blank=True, null=True)
    profession = models.CharField(max_length=200, blank=True, null=True)
    profile_picture = models.ImageField(max_length=200, default='profile.png', upload_to=user_directory_path)
    github = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    x = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
