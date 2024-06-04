from rest_framework import viewsets, permissions

from posts.api.serializers import PostSerializer
from posts.api.permissions import IsOwnerOrReadOnly

from posts.models import Post

# Post viewset
class PostviewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
