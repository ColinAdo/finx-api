from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom user model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    header = models.CharField(max_length=200, blank=True, null=True)
    profession = models.CharField(max_length=200, blank=True, null=True)
    profile_picture = models.URLField(
        null=True, blank=True, 
        default='https://files.edgestore.dev/8wg333ckwaulnstn/publicFiles/_public/d0b20548-718a-4f7d-8916-4ee4e7d6f421.png'
    )
    github = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    x = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
