from rest_framework import serializers

from chats.models import Chat, Contact, Message

from accounts.api.serializers import UserSerializer

#  Contact serialiser class 
class ContactSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'

#  Message serialiser class 
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


#  Chat serialiser class 
class ChatSerializer(serializers.ModelSerializer):
    participants = ContactSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Chat
        fields = '__all__'
