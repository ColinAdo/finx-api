from rest_framework import serializers

from posts.models import Post
from comments.api.serializers import CommentSerializer
from likes.api.serializers import LikeSerializer

# Post serializer
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()

    likes = LikeSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def get_comments_count(self, obj):
        return obj.comments.count()

    class Meta:
        model = Post
        fields = (
            'id',
            'file',
            'caption',
            'created_at',
            'comments',
            'comments_count',
            'likes',
            'likes_count'
        )

