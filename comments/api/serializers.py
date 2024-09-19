from rest_framework import serializers

from comments.models import Comment
from accounts.api.serializers import UserSerializer

# Comment serializer
class CommentSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = (
            'id', 
            'comment',
            'comment_image',
            'created_at',
            'owner',
            'post'
        )