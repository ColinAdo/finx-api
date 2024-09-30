from rest_framework import serializers

from bookmark.models import Bookmark

# Bookmark post serializer
class BookmarkSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    # post = serializers.SerializerMethodField()
    # user = serializers.PrimaryKeyRelatedField(read_only=True)
    # post = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Bookmark
        fields = fields = ['id', 'user', 'post'] 

    def get_user(self, obj):
        return {
            'id': obj.user.id,
            'username': obj.user.username,
            'profile_picture': obj.user.profile_picture if obj.user.profile_picture else None,
        }

    # def get_post(self, obj):
    #     return {
    #         'id': obj.follows.id,
    #         'username': obj.follows.username,
    #         'profile_picture': obj.follows.profile_picture if obj.follows.profile_picture else None,
    #     }
