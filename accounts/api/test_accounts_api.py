from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

from accounts.api.serializers import UserSerializer

# Test users api
class UserApiTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.User = get_user_model()
        cls.user = cls.User.objects.create(
            username="TestUser",
            email="TestUser@example.com",
            password="TestUser",
        )
        cls.access_token = AccessToken.for_user(cls.user)

    def test_get_users(self):
        url = reverse("users")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(url, format="json")

        queryset = self.User.objects.all()
        expected_data = UserSerializer(queryset, many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data, expected_data)
        self.assertContains(response, self.user)


    def test_retrieve_users(self):
        url = reverse("user-detail", kwargs={"pk": self.user.id})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(url, format="json")

        obj = self.User.objects.get(pk=self.user.id)
        expected_data = UserSerializer(obj).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
        self.assertContains(response, self.user)