from django.db import models

from accounts.models import CustomUser

# upload directory path
def user_directory_path(instance, filename):
    return "profile/{0}/{1}".format(instance.owner.username, filename)


class Profile(models.Model):
    owner = models.OneToOneField(CustomUser, related_name='profile_data', on_delete=models.CASCADE)
    header = models.CharField(max_length=200, blank=True, null=True)
    profession = models.CharField(max_length=200, blank=True, null=True)
    profile_picture = models.ImageField(max_length=200, default="profile.png", upload_to=user_directory_path)
    github = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    x = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.owner.username
    

