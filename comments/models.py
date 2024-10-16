from django.db import models
from django.conf import settings

from posts.models import Post

# Comment model
class Comment(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    comment = models.CharField(max_length=4000, blank=True, null=True)
    comment_image = models.CharField(max_length=4000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[:20]
