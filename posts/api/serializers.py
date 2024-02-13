from rest_framework import serializers

from ..models import Post, Comment
from accounts.api.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    likes = UserSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()

    liked_by_logged_in_user = serializers.SerializerMethodField()

    comments = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "file",
            "caption",
            "created_at",
            "author",
            "likes",
            "likes_count",
            "liked_by_logged_in_user",
            "comments",
            "comments_count",
        )

    def get_likes_count(self, obj):
        return len(obj.likes.all())

    def get_liked_by_logged_in_user(self, obj):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user
            return user in obj.likes.all()
        return False
    
    def get_comments(self, obj):
        comments = obj.comment_set.all()
        return CommentSerializer(comments, many=True).data

    def get_comments_count(self, obj):
        return len(obj.comment_set.all())
