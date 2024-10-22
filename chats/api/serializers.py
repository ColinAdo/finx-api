from rest_framework import serializers

from chats.models import Conversation, ConversationMessage
from accounts.api.serializers import UserSerializer

#  Contact serialiser class 
class ConversationSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ('id', 'users', 'modified_at',)

#  Message serialiser class 
class ConversationMessageSerializer(serializers.ModelSerializer):
    sent_to = UserSerializer(many=False, read_only=True)
    created_by = UserSerializer(many=False, read_only=True)

    class Meta:
        model = ConversationMessage
        fields = ('id', 'body', 'sent_to', 'created_by',)