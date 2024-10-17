import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from accounts.api.serializers import UserSerializer

# Chat Consumer
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        user = self.scope.get('user')
        if not user.is_authenticated:
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
        data_source = data.get('source')

        print("Received", json.dumps(data, indent=2))

        if data_source == 'update_profile_picture':
            self.receive_profile_picture(data)

    def receive_profile_picture(self, data):
        user = self.scope.get('user')
        filename = data.get('profile_picture')
        if filename:
            user.profile_picture = filename
            user.save()

            serialized = UserSerializer(user)

            # Broadcast updated profile picture to the group
            self.send_group(self.username, 'update_profile_picture', serialized.data)

    def send_group(self, group, source, data):
        response = {
            'type': 'profile_picture_updated',
            'source': source,
            'profile_picture': data['profile_picture']
        }
        async_to_sync(self.channel_layer.group_send)(
            group, response
        )


    def profile_picture_updated(self, event):
        profile_picture_data = event['profile_picture']

        # Send updated profile data to the connected client
        self.send(text_data=json.dumps({
            'type': 'profile_picture_updated',
            'profile_picture': profile_picture_data
        }))
