from profiles.models import Profile

from rest_framework import serializers

class ProfileSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Profile
        fields = '__all__'