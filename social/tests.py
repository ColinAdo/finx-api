from django.test import TestCase

from accounts.models import CustomUser
from social.models import UserFollow

# User follow test case
class TestUserFollowers(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = CustomUser.objects.create(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

        cls.user2 = CustomUser.objects.create(
            username='testuser2',
            email='testuser@example.com2',
            password='testpassword2'
        )

        cls.follow = UserFollow.objects.create(
            user=cls.user1,
            follows=cls.user2,
        )

    def test_follow_data(self):
        self.assertEqual(UserFollow.objects.count(), 1)
        self.assertEqual(self.follow.user, self.user1)
        self.assertEqual(self.follow.follows, self.user2)
        self.assertEqual(str(self.follow), f'{self.user1} followers')
