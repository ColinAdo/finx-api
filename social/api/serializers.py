from rest_framework import serializers

from social.models import UserFollow

# UserFollow serializer
class UserFollowSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(read_only=True)
    # follows = serializers.PrimaryKeyRelatedField(read_only=True)
    user = serializers.SerializerMethodField()
    follows = serializers.SerializerMethodField()

    class Meta:
        model = UserFollow
        fields = fields = ['id', 'user', 'follows'] 

    def get_user(self, obj):
        return {
            'id': obj.user.id,
            'username': obj.user.username,
            'profile_picture': obj.user.profile_picture if obj.user.profile_picture else None,
        }

    def get_follows(self, obj):
        return {
            'id': obj.follows.id,
            'username': obj.follows.username,
            'profile_picture': obj.follows.profile_picture if obj.follows.profile_picture else None,
        }