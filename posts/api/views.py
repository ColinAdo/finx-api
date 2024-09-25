from django.contrib.auth import get_user_model

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

    @action(detail=False, methods=['get'], url_path='author-posts/(?P<username>[^/.]+)')
    def get_author_posts(self, request, username=None):
        User = get_user_model()
       
        try:
            author = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=404)
        
        author_posts = Post.objects.filter(author=author).order_by('-created_at')
        
        serializer = self.get_serializer(author_posts, many=True)
        return Response(serializer.data)
