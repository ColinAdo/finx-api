from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Contact, Message


class TestContact(TestCase):

    @classmethod
    def setUpTestData(cls):

        User = get_user_model()
        cls.user1 = User.objects.create(
            username="test1",
            email="test1@example.com",
        )

        cls.user2 = User.objects.create(
            username="test2",
            email="test2@example.com",
        )
        cls.contact1 = Contact.objects.create(user=cls.user1)

    def test_contact_content(self):
        contact = Contact.objects.all().count()
        user_contact = self.user1.contact_set.all().count()

        self.assertEqual(contact, 1)
        self.assertEqual(self.contact1.user, self.user1)
        self.assertEqual(user_contact, 1)

    def test_contact_without_friends(self):
        contact = self.contact1.friends.all().count()

        self.assertEqual(contact, 0)

    def test_contact_friends_relationship(self):
        contact2 = Contact.objects.create(user=self.user2)
        self.contact1.friends.add(contact2)
        number_of_friends = self.contact1.friends.all().count()

        self.assertEqual(number_of_friends, 1)
        self.assertIn(self.contact1, contact2.friends.all())
        self.assertIn(contact2, self.contact1.friends.all())

    def test__return_string(self):
        self.assertEqual(str(self.contact1), self.user1.username)


class TestMessage(TestCase):

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.user = User.objects.create(
            username="test1",
            email="test1@example.com",
        )

        cls.contact = Contact.objects.create(user=cls.user)
        cls.message = Message.objects.create(contact=cls.contact, content="Test Message")


    def test_message_content(self):

        self.assertEqual(Message.objects.all().count(), 1)
        self.assertEqual(self.message.contact.user, self.user)
        self.assertEqual(self.message.content, "Test Message")

    def test_return_string(self):
        self.assertEqual(str(self.message), self.contact.user.username)