from rest_framework import serializers

from comments.models import Comment

# Comment serializer
class CommentSerializer(serializers.ModelSerializer):
    commented_by = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Comment
        fields = (
            'id', 
            'comment',
            'comment_image',
            'created_at',
            'commented_by',
            'post'
        )