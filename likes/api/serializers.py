from rest_framework import serializers

from likes.models import LikePost

# Like post serializer
class LikeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = LikePost
        fields = '__all__'
