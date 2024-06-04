from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions

from chats.api.serializers import ChatSerializer, MessageSerializer
from core.authentications import CustomJWTAuthentication    

from chats.models import Chat, Contact, Message

# Helper function to get user contact
def get_user_contact(username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    contact = get_object_or_404(Contact, user=user)
    return contact


# Chat list view
class ChatListCreateView(generics.ListAPIView):
    serializer_class = ChatSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Chat.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            contact = get_user_contact(username)
            queryset = contact.chats.all()
        return queryset

# Chat detail view
class ChatDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

# Chat message view
class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessageSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        message_id = self.kwargs['message_pk']
        queryset = get_object_or_404(Message, id=message_id)
        return queryset
