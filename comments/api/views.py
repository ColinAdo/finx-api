from rest_framework import viewsets, permissions

from .serializers import CommentSerializer
from comments.models import Comment
from profiles.api.permissions import IsOwnerOrReadOnly

# Comment viewset
class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
