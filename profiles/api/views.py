from rest_framework import viewsets, permissions

from profiles.models import Profile
from .serializers import ProfileSerializers
from .permissions import IsOwnerOrReadOnly

# Profile viewset
class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)