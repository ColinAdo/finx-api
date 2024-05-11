from django.test import TestCase
from django.contrib.auth import get_user_model

# Test User model
class UserTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.User = get_user_model()
        cls.User.objects.create(
            username="testuser",
            email="testuser@example.com",
            password="admin1111"
        )


    def test_user_fields(self):
        user = self.User.objects.get(id=1)
        
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertEqual(user.password, "admin1111")

    def test_resturn_string(self):
        self.assertEqual(str(self.User.objects.get(id=1)), "testuser")
