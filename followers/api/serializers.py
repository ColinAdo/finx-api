from rest_framework import serializers

from followers.models import UserFollow

class UserFollowSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    follows = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = UserFollow
        fields = '__all__'