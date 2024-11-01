from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Conversation, ConversationMessage

# Test contact test case
class TestConversation(TestCase):

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
        users = [cls.user1, cls.user2]
        cls.conversation1 = Conversation.objects.create(users=users)

    def test_conversation_content(self):
        conversation = Conversation.objects.all().count()
        user_contact = self.user1.conversations_set.all().count()

        self.assertEqual(conversation, 1)
        self.assertEqual(self.conversation1.users, [self.user1, self.user2])
        self.assertEqual(user_contact, 1)

# Test for conversation messages
class TestMessage(TestCase):

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

        cls.conversation = Conversation.objects.create(user=[cls.user1, cls.user2])
        cls.message = ConversationMessage.objects.create(
            conversation=cls.conversation, body="Test Message", created_by=cls.user1, sent_to=cls.user2)

    def test_message_content(self):

        self.assertEqual(ConversationMessage.objects.all().count(), 1)
        self.assertEqual(self.message.conversation.users, [self.user1, self.user2])
        self.assertEqual(self.message.body, "Test Message")
        self.assertEqual(str(self.message), f'{self.user1} => {self.user2}')

