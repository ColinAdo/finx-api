from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from chats.api.serializers import ChatSerializer
from chats.models import Chat, Contact, Message

# Test chat test case
class ChatApiTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.user1 = User.objects.create(
            username="TestUser",
            email="test@example.com",
            password="Testpassword"
        )
        cls.user2 = User.objects.create(
            username="TestUser2",
            email="test@example.com2",
            password="Testpassword2"
        )

        cls.contact1 = Contact.objects.create(
            user=cls.user1,
        )
        cls.contact2 = Contact.objects.create(
            user=cls.user2,
        )

        cls.contact1.friends.add(cls.contact2)

        cls.chat = Chat.objects.create()
        cls.chat.participants.add(cls.contact1)
        cls.chat.participants.add(cls.contact2)

        cls.access_token = AccessToken.for_user(cls.user1)

    def test_get_all_chats(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        url = reverse("chats")
        response = self.client.get(url, format="json")

        chat = Chat.objects.get(participants=self.contact1)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Chat.objects.count(), 1)
        self.assertEqual(chat.messages.count(), 0)

    def test_get_all_chat_messages(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        message = Message.objects.create(
            contact=self.contact2,
            content="This message one"
        )

        self.chat.messages.add(message)

        url = reverse("chats")
        response = self.client.get(url, format="json")

        chat = Chat.objects.get(participants=self.contact1)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Chat.objects.count(), 1)
        self.assertEqual(chat.messages.count(), 1)
        self.assertEqual(chat.participants.count(), 2)

    def test_retrieve_chat(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        url = reverse("chat-detail", kwargs={"pk": self.chat.id})
        response = self.client.get(url, format="json")

        obj = Chat.objects.get(id=self.chat.id)
        expected_data = ChatSerializer(obj).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
        self.assertContains(response, self.user1)
        self.assertContains(response, self.user2)
