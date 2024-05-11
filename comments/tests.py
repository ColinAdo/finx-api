from django.test import TestCase

from comments.models import Comment
from posts.models import Post
from accounts.models import CustomUser

class TestComment(TestCase):
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

        cls.comment = Comment.objects.create(
            owner=cls.user,
            post=cls.post,
            comment="First comment"
        )

    def test_comment_data(self):
        comment = Comment.objects.get(id=1)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(comment.owner, self.user)
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.comment, self.comment.comment)

    def test_return_string(self):
        self.assertEqual(str(self.comment), self.comment.comment)
