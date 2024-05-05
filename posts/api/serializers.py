from rest_framework import serializers

from posts.models import Post
from comments.api.serializers import CommentSerializer

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "file",
            "caption",
            "created_at",
            'comments'
        )

