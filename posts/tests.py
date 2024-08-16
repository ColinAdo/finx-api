from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post

# Post test case
class TestPost(TestCase):

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.user1 = User.objects.create(
            username='testuser1',
            email='testuser1@example.com'
        )

        cls.post = Post.objects.create(
            author=cls.user1,
            caption='Caption'
        )

    def test_post_contents(self):
        post = Post.objects.all().count()

        self.assertEqual(self.post.author, self.user1)
        self.assertEqual(self.post.caption, 'Caption')
        self.assertEqual(post, 1)


    def test_get_file_type(self):
        post = Post.objects.get(id=1)
        post.file = 'posts/tests.png'
        post.save()

        self.assertEqual(post.file, 'posts/tests.png')
        self.assertEqual(post.get_file_type(), 'image')

    def test_return_string(self):
        self.assertEqual(str(self.post), self.user1.username)

 
