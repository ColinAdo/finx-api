from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

from social.models import UserFollow

# User follow test case
class TestUserFollow(APITestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.user1 = User.objects.create(
            username='testuser1',
            email='testuser1@example.com',
            password='testpassword',
        )
        cls.user2 = User.objects.create(
            username='testuser2',
            email='testuser2@example.com',
            password='testpassword',
        )
        cls.acccess_token = AccessToken.for_user(cls.user1)

    def test_follow_user(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.acccess_token}')
        url = reverse('follow-unfollow', kwargs={'pk': self.user1.id})
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(UserFollow.objects.count(),1)
