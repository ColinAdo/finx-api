from django.conf import settings
from django.db import models
from shortuuid.django_fields import ShortUUIDField

import magic

class Post(models.Model):
    uuid = ShortUUIDField(max_length=10, length=10, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to="posts", blank=True)
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

