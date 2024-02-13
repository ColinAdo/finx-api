from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


from posts.models import Post
from posts.api.serializers import PostSerializer


class TestPostsApiListView(APITestCase):

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

    def test_get_posts_list(self):
        url = reverse("posts")
        response = self.client.get(url, format="json")

        queryset = Post.objects.all()

        expected_data = PostSerializer(queryset, many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
        self.assertEqual(queryset.count(), 1)
        self.assertContains(response, str(self.user.id))
