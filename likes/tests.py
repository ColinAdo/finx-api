from django.test import TestCase

from accounts.models import CustomUser
from posts.models import Post
from likes.models import LikePost


class TestLikePost(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.create(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

        cls.post = Post.objects.create(
            author=cls.user,
            caption='first post',
        )

        cls.like = LikePost.objects.create(
            user=cls.user,
            post=cls.post,
        )

    def test_like_post(self):
        self.assertEqual(LikePost.objects.count(), 1)
        self.assertEqual(self.like.user, self.user)
        self.assertEqual(self.like.post, self.post)
        self.assertEqual(str(self.like), f'{self.user.username} likes')
