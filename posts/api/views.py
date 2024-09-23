from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from posts.api.serializers import PostSerializer
from posts.api.permissions import IsOwnerOrReadOnly

from posts.models import Post

# Post viewset
class PostviewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['get'], url_path='author-posts')
    def get_author_posts(self, request, pk=None):
        post = self.get_object()
        
        author_posts = Post.objects.filter(author=post.author).exclude(id=post.id).order_by('-created_at')
        
        serializer = self.get_serializer(author_posts, many=True)
        
        return Response(serializer.data)
