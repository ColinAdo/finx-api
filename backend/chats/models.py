from django.conf import settings
from django.db import models

class Contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.user.username
    

