from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        user = self.scope.get('user')
        if not user.is_authenticated: 
            self.close()
            return
        print('Logged in user:', user)
        self.accept()

    def disconnect(self, close_code):
        pass
