import json
from asgiref.sync import async_to_sync
from asgiref.sync import sync_to_async
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

from accounts.api.serializers import UserSerializer
from .models import ConversationMessage

# Thumbnail consumer
class ThumbnailConsumer(WebsocketConsumer):
    def connect(self):
        user = self.scope.get('user')
        if not user or not user.is_authenticated:
            self.close()
            return

        self.username = user.username
        async_to_sync(self.channel_layer.group_add)(
            self.username, self.channel_name
        )
        self.accept()
        print(f"{self.username} connected")

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.username, self.channel_name
        )
        print(f"{self.username} disconnected")

    def receive(self, text_data):
        data = json.loads(text_data)
        data_source = data.get('type')

        print("Received", json.dumps(data, indent=2))

        if data_source == 'update_profile_picture':
            self.receive_profile_picture(data)

    def receive_profile_picture(self, data):
        user = self.scope.get('user')
        filename = data.get('profile_picture')
        
        if filename and user:
            user.profile_picture = filename
            user.save()

            serialized = UserSerializer(user)

            self.send_group(self.username, serialized.data)

    def send_group(self, group, data):
        async_to_sync(self.channel_layer.group_send)(
            group,
            {
                'type': 'profile_picture_updated', 
                'profile_picture': data,
            }
        )

    def profile_picture_updated(self, event):
        profile_picture_data = event['profile_picture']

        self.send(text_data=json.dumps({
            'type': 'profile_picture_updated',
            'profile_picture': profile_picture_data,
        }))

# Chat consumer
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Join room
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self):
        # Leave room

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Recieve message from web sockets
    async def receive(self, text_data):
        data = json.loads(text_data)
        print("Received", json.dumps(data, indent=2))

        conversation_id = data['data']['conversation_id']
        sent_to_id = data['data']['sent_to_id']
        name = data['data']['name']
        body = data['data']['body']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'body': body,
                'name': name
            }
        )

        await self.save_message(conversation_id, body, sent_to_id)
    
    # Sending messages
    async def chat_message(self, event):
        body = event['body']
        name = event['name']

        await self.send(text_data=json.dumps({
            'body': body,
            'name': name
        }))

    @sync_to_async
    def save_message(self, conversation_id, body, sent_to_id):
        user = self.scope['user']

        ConversationMessage.objects.create(conversation_id=conversation_id, body=body, sent_to_id=sent_to_id, created_by=user)