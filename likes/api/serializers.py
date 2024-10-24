from rest_framework import serializers

from likes.models import LikePost

# Like post serializer
class LikeSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    class Meta:
        model = LikePost
        fields = fields = ['id', 'user', 'post'] 

    def get_user(self, obj):
        return {
            'id': obj.user.id,
            'username': obj.user.username,
            'profile_picture': obj.user.profile_picture if obj.user.profile_picture else None,
        }
