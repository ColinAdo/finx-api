from django.conf import settings
from django.db import models

import magic

def user_directory_path(instance, filename):
    return "posts/{0}/{1}".format(instance.author.username, filename)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path, blank=True)
    caption = models.TextField(blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="likes")
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
    

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} commented on this post"
