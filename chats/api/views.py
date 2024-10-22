from rest_framework import permissions, viewsets, status
from rest_framework.response import Response

from chats.models import Conversation
from chats.api.serializers import (
    ConversationSerializer, 
    ConversationMessageSerializer)

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

