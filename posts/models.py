from django.conf import settings
from django.db import models

import magic

# Post model
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fileUrl = models.URLField(null=True,blank=True)
    caption = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
        

    def __str__(self):
        return self.author.username
    