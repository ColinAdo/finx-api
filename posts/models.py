from django.conf import settings
from django.db import models
from shortuuid.django_fields import ShortUUIDField

import magic

def user_directory_path(instance, filename):
    return "posts/{0}/{1}".format(instance.author.username, filename)


class Post(models.Model):
    uuid = ShortUUIDField(max_length=10, length=10, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path, blank=True)
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_file_type(self):
        file_path = self.file.path
        mime = magic.from_file(file_path, mime=True)

        if mime.startswith("image"):
            return "image"
        elif mime.startswith("video"):
            return "video"
        else:
            return "unknown file type"
        

    def __str__(self):
        return self.author.username

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ["user", "post"]

    def __str__(self):
        return f"{self.user.username} liked the post"
