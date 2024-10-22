from rest_framework import permissions, viewsets, status
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from chats.models import Conversation
from chats.api.serializers import (
    ConversationSerializer, 
    ConversationMessageSerializer)

User = get_user_model()

class ConversationViewSet(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.conversations.all()
    
    def retrieve(self, request, pk=None):
        """
        Override the retrieve method to return conversation details
        along with its messages.
        """
        try:
            conversation = self.request.user.conversations.get(pk=pk)
        except Conversation.DoesNotExist:
            return Response(
                {"detail": "Conversation not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Serialize the conversation and its messages
        conversation_serializer = ConversationSerializer(conversation)
        messages_serializer = ConversationMessageSerializer(conversation.messages.all(), many=True)

        return Response({
            'conversation': conversation_serializer.data,
            'messages': messages_serializer.data
        })

    def create(self, request, *args, **kwargs):
        """
        Override the create method to check if a conversation already exists 
        between the logged-in user and the specified user.
        """
        # Get the list of users from the request data
        users_ids = request.data.get('users', [])

        if len(users_ids) != 2:
            return Response(
                {"detail": "You must provide exactly two user IDs."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Ensure both users exist
            users = User.objects.filter(id__in=users_ids)
            if users.count() != 2:
                return Response(
                    {"detail": "One or more users do not exist."},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Check if a conversation already exists between these two users
            existing_conversation = Conversation.objects.filter(users__in=users).distinct()
            if existing_conversation.exists():
                return Response(
                    {"id": existing_conversation.first().id},
                    status=status.HTTP_200_OK
                )

            # Create a new conversation if none exists
            conversation = Conversation.objects.create()
            conversation.users.set(users)
            conversation.save()

            serializer = self.get_serializer(conversation)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except User.DoesNotExist:
            return Response(
                {"detail": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )