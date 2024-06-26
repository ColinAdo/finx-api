from rest_framework import serializers

from social.models import UserFollow

# UserFollow serializer
class UserFollowSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    follows = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = UserFollow
        fields = '__all__'