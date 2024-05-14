from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken


from posts.models import Post
from posts.api.serializers import PostSerializer


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
        cls.access_token = AccessToken.for_user(cls.user)

    def test_create_posts(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        url = reverse('posts-list')
        data = {
            "author": self.user.id,
            "caption": "This is a test post2"
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)

    def test_get_all_posts(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        url = reverse("posts-list")
        response = self.client.get(url, format="json")

        queryset = Post.objects.all()
        expected_data = PostSerializer(queryset, many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
        self.assertEqual(len(response.data), 1)
        self.assertContains(response, str(self.user.id))

    def test_retrieve_post(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        url = reverse("posts-detail", kwargs={"pk": self.post.id})
        response = self.client.get(url)

        obj = Post.objects.get(id=self.post.id)
        expected_data = PostSerializer(obj).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
        self.assertContains(response, self.post.caption)

    def test_update_post(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        url = reverse("posts-detail", kwargs={"pk": self.post.id})
        data = {
            "author": self.user.id,
            "caption": "updated caption",
        }
        response = self.client.put(url, data, format='json')

        self.post.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.post.caption, "updated caption")

    def test_delete_post(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        url = reverse("posts-detail", kwargs={"pk": self.post.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)

