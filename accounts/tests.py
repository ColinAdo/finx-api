from django.test import TestCase
from django.contrib.auth import get_user_model

# Follow and unfollow test cases 
class FollowActivityTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.User = get_user_model()
        cls.User.objects.create(
            username="testuser",
            email="testuser@example.com"
        )

        cls.User.objects.create(
            username="test2user",
            email="test2user@example.com"
        )

    def test_follow(self):
        userOne = self.User.objects.get(id=1)
        userTwo = self.User.objects.get(id=2)
        userOne.follow(userTwo)

        following = userOne.is_following(userTwo)
        following_count = userOne.followers.all().count()


        self.assertEqual(following_count, 1)
        self.assertEqual(following, True)

    def test_unfollow(self):
        userOne = self.User.objects.get(id=1)
        userTwo = self.User.objects.get(id=2)
        userOne.follow(userTwo)

        userOne.unfollow(userTwo)
        following = userOne.followers.all().count()
        is_following = userOne.is_following(userTwo)

        self.assertEqual(following, 0)
        self.assertEqual(is_following, False)

    def test_is_follow(self):
        userOne = self.User.objects.get(id=1)
        userTwo = self.User.objects.get(id=2)
        userOne.follow(userTwo)

        following = userOne.is_following(userTwo)
        self.assertEqual(following, True)
