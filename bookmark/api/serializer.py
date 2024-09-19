from rest_framework import serializers

from bookmark.models import Bookmark

# Bookmark post serializer
class BookmarkSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Bookmark
        fields = '__all__'
