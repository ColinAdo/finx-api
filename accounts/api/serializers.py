from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# User serializer
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 
            'username', 
            'email',
            'bio',
            'profile_picture',
            'website',
            'gender',
            'date_joined',
        )

    # def get_profile_picture(self, obj):
    #     request = self.context.get('request', None)  # Safely get the request object
    #     if request and obj.profile_picture and hasattr(obj.profile_picture, 'url'):
    #         return request.build_absolute_uri(obj.profile_picture.url)  # Build absolute URI
    #     return None  # Return None if there's no request or profile picture
