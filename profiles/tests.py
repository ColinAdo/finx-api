from django.test import TestCase
from profiles.models import Profile
from accounts.models import CustomUser

# Profile test case
class TestProfile(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.create(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )


    def test_create_user(self):
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(self.user.username, 'testuser')

    def test_profile_data(self):
        profile = Profile.objects.filter(owner=self.user).first()
        profile.header = 'Expert software developer'
        profile.save()

        self.assertIsNotNone(profile, "Profile should exist")
        self.assertEqual(profile.owner.username, 'testuser')
        self.assertEqual(profile.profile_picture, 'profile.png')
        self.assertEqual(profile.header, 'Expert software developer')
