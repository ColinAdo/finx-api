from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post


class TestPost(TestCase):

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.user = User.objects.create(
            username="testuser",
            email="testuser@example.com"
        )

        cls.post = Post.objects.create(
            author=cls.user,
            caption="Caption"
        )

    def test_post_contents(self):
        post = Post.objects.all().count()

        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.caption, "Caption")
        self.assertEqual(post, 1)

    def test_get_file_type(self):
        post = Post.objects.get(id=1)
        post.file = "posts/tests.png"
        post.save()

        self.assertEqual(post.file, "posts/tests.png")
        self.assertEqual(post.get_file_type(), "image")

    def test_return_string(self):
        self.assertEqual(str(self.post), self.user.username)