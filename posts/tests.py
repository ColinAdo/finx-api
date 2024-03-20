from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post, Comment

class TestPost(TestCase):

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.user1 = User.objects.create(
            username="testuser1",
            email="testuser1@example.com"
        )
        cls.user2 = User.objects.create(
            username="testuser2",
            email="testuser2@example.com"
        )

        cls.post = Post.objects.create(
            author=cls.user1,
            caption="Caption"
        )

    def test_post_contents(self):
        post = Post.objects.all().count()

        self.assertEqual(self.post.author, self.user1)
        self.assertEqual(self.post.caption, "Caption")
        self.assertEqual(post, 1)

    def test_post_likes(self):
        post = Post.objects.get(id=1)
        post.likes.add(self.user2)

        self.assertEqual(post.likes.all().count(), 1)
        self.assertEqual(self.user2.likes.all().count(), 1)
        self.assertNotIn(self.user1, post.likes.all())
        self.assertIn(self.user2, post.likes.all())

    def test_get_file_type(self):
        post = Post.objects.get(id=1)
        post.file = "posts/tests.png"
        post.save()

        self.assertEqual(post.file, "posts/tests.png")
        self.assertEqual(post.get_file_type(), "image")

    def test_return_string(self):
        self.assertEqual(str(self.post), self.user1.username)

    def test_get_following_posts(self):
        self.user2.follow(self.user1)
        following_post = self.user1.get_following_posts()
        self.assertEqual(self.user2.is_following(self.user1), True)
        self.assertEqual(following_post.count(), 1)


class TestComment(TestCase):

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.user1 = User.objects.create(
            username="testuser1",
            email="testuser1@example.com"
        )
        cls.user2 = User.objects.create(
            username="testuser2",
            email="testuser2@example.com"
        )

        cls.post = Post.objects.create(
            author=cls.user1,
            caption="Caption"
        )

    def test_commenting_on_post(self):
        comment = Comment.objects.create(
            user=self.user2,
            post=self.post,
            content="This is a test comment"
        )

        commented_by = comment.user.username

        self.assertEqual(commented_by, self.user2.username)
        self.assertEqual(comment.post, self.post)
        self.assertEqual(self.user2.comment_set.all().count(), 1)
        self.assertEqual(self.post.comment_set.all().count(), 1)

    def test_return_string(self):
        comment = Comment.objects.create(
            user=self.user2,
            post=self.post
        )
        self.assertEqual(
            str(comment), f"{self.user2.username} commented on this post")
