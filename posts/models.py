from django.conf import settings
from django.db import models

import magic

# user dir path
def user_directory_path(instance, filename):
    return 'posts/{0}/{1}'.format(instance.author.username, filename)

# Post model
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fileUrl = models.FileField(upload_to=user_directory_path)
    caption = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_file_type(self):
        file_path = self.file.path
        mime = magic.from_file(file_path, mime=True)

        if mime.startswith('image'):
            return 'image'
        elif mime.startswith('video'):
            return 'video'
        else:
            return 'unknown file type'
        

    def __str__(self):
        return self.author.username
    