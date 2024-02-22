from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

from accounts.api.serializers import UserSerializer


class TestUserApiListView(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.User = get_user_model()
        cls.user = cls.User.objects.create(
            username="TestUser",
            email="TestUser@example.com",
            password="TestUser",
        )

    def test_get_users_list(self):
        response = self.client.get(reverse("users"), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_expected_data(self):
        response = self.client.get(reverse("users"), format="json")
        queryset = self.User.objects.all()

        expected_data = UserSerializer(queryset, many=True).data

        for user_data in expected_data:
            user_data['profile_picture'] = f"http://testserver{user_data['profile_picture']}"

        self.assertEqual(queryset.count(), 1)
        self.assertEqual(response.data, expected_data)
        self.assertContains(response, self.user)


class TestUserApiDetailView(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.User = get_user_model()
        cls.user = cls.User.objects.create(
            username="TestUser",
            email="TestUser@example.com",
            password="TestUser",
        )

    def test_user_get_status(self):
        response = self.client.get(
            reverse("user-detail", kwargs={"pk": self.user.id}),
            format="json")

        obj = self.User.objects.get(pk=self.user.id)
        expected_data = UserSerializer(obj).data

        expected_data["profile_picture"] = f"http://testserver{expected_data['profile_picture']}"

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
        self.assertContains(response, self.user)
