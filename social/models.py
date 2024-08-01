from django.conf import settings
from django.db import models

# User follow  model 
class UserFollow(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='src_follow', on_delete=models.CASCADE)
    follows = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='des_follow', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} followers'