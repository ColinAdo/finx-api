from rest_framework import serializers

from bookmark.models import Bookmark

# Bookmark post serializer
class BookmarkSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    class Meta:
        model = Bookmark
        fields = fields = ['id', 'user', 'post'] 

    def get_user(self, obj):
        return {
            'id': obj.user.id,
            'username': obj.user.username,
            'profile_picture': obj.user.profile_picture if obj.user.profile_picture else None,
        }
