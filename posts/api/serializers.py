from rest_framework import serializers

from posts.models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            "id",
            "file",
            "caption",
            "created_at",
        )

