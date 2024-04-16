from django.contrib.auth.models import AbstractUser
from django.db import models

from posts.models import Post

def user_directory_path(instance, filename):
    return "profile/{0}/{1}".format(instance.username, filename)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255)
    header = models.CharField(max_length=200, blank=True, null=True)
    # profession = models.CharField(max_length=200, blank=True, null=True)
    # location = models.CharField(max_length=200, blank=True, null=True)
    profile_picture = models.ImageField(max_length=200, default="profile.png", upload_to=user_directory_path)
    github = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    x = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    def follow(self, user):
        if not self.is_following(user):
            return self.followers.add(user)

    def unfollow(self, user):
        if self.is_following(user):
            return self.followers.remove(user)

    def is_following(self, user):
        return self.followers.filter(id=user.id).exists()
    
    def get_following_posts(self):
        followed_ids = self.followers.values_list('id', flat=True)
        return Post.objects.filter(author_id__in=followed_ids) | Post.objects.filter(author_id=self.id)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
