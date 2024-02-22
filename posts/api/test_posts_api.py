from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


from posts.models import Post, Comment
from posts.api.serializers import PostSerializer, CommentSerializer


class PostsApiTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.User = get_user_model()
        cls.user = cls.User.objects.create(
            username="TestUser",
            email="TestEmail@example.com",
            password="TestPassword"
        )

        cls.post = Post.objects.create(
            author=cls.user,
            caption="This is a test post"
        )

        cls.comment = Comment.objects.create(
            user=cls.user,
            post=cls.post,
            content="This is a test comment1"
        )

    def test_post_posts(self):
        url = reverse('posts-list')
        data = {
            "author": self.user.id,
            "caption": "This is a test post2"
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)

    def test_get_posts(self):
        url = reverse("posts-list")
        response = self.client.get(url, format="json")

        queryset = Post.objects.all()
        expected_data = PostSerializer(queryset, many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
        self.assertEqual(len(response.data), 1)
        self.assertContains(response, str(self.user.id))

    def test_retrieve_posts(self):
        url = reverse("posts-detail", kwargs={"pk": self.post.id})
        response = self.client.get(url)

        obj = Post.objects.get(id=self.post.id)
        expected_data = PostSerializer(obj).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
        self.assertContains(response, "This is a test post")

    def test_post_posts_comment(self):
        url = reverse("comments", kwargs={"pk": self.post.id})
        data = {
            "user": self.user.id,
            "post": self.post.id,
            "content": "This is a test comment"
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 2)

    def test_get_posts_comments(self):
        url = reverse("comments", kwargs={"pk": self.post.id})
        response = self.client.get(url, format="json")

        queryset = Comment.objects.all()
        expected_data = CommentSerializer(queryset, many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(response.data, expected_data)
        self.assertEqual(len(response.data), 1)
        self.assertContains(response, "This is a test comment1")

    def test_retrieve_post_comments(self):
        url = reverse(
            "comment-detail", 
            kwargs={
                "pk": self.post.id, 
                "comment_pk": self.comment.id
                }
            )
        response = self.client.get(url, format="json")

        obj = Comment.objects.get(id=self.comment.id)
        expected_data = CommentSerializer(obj).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
