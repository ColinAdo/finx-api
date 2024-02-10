from django.shortcuts import get_object_or_404
from rest_framework import generics

from .serializers import PostSerializer, CommentSerializer

from ..models import Post, Comment

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['pk']
        queryset = Comment.objects.filter(post_id=post_id)
        return queryset
    

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer    

    def get_object(self):
        comment_id = self.kwargs['comment_pk']
        obj = get_object_or_404(id=comment_id)
        return obj
