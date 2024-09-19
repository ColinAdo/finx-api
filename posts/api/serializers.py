from rest_framework import serializers

from posts.models import Post
from comments.api.serializers import CommentSerializer
from likes.api.serializers import LikeSerializer
from accounts.api.serializers import UserSerializer
from bookmark.api.serializer import BookmarkSerializer

# Post serializer
class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()

    likes = LikeSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    bookmarks = BookmarkSerializer(many=True, read_only=True)
    bookmark_count = serializers.SerializerMethodField()


    def get_bookmark_count(self, obj):
        return obj.bookmarks.count()
    
    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def get_comments_count(self, obj):
        return obj.comments.count()

    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'fileUrl',
            'caption',
            'created_at',
            'comments',
            'comments_count',
            'likes',
            'likes_count',
            'bookmarks',
            'bookmark_count'
        )

