from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics

from .serializer import BookmarkSerializer
from posts.models import Post
from posts.api.serializers import PostSerializer
from bookmark.models import Bookmark

User = get_user_model()

# Bookmark post view
class BookmarkView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookmarkSerializer

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            bookmark_post = Bookmark.objects.filter(user=user)

            serializer = BookmarkSerializer(bookmark_post, many=True)
            return Response({'success': True, 'bookmark_post': serializer.data})

        except ObjectDoesNotExist:
            return Response({'success': False, 'message': 'post does not exist'})
        
    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            new_bookmark_post = Bookmark.objects.get_or_create(user=request.user, post=post)

            if not new_bookmark_post[1]:
                new_bookmark_post[0].delete()
                return Response({'success': True, 'message': 'post saved'})
            else:
                return Response({'success': True, 'message': 'post saved'})
            
        except ObjectDoesNotExist:
            return Response({ 'success': False, 'message': 'post does not exist' })

class BookmarkedPostsView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        username = self.kwargs.get('username')
        user = User.objects.filter(username=username).first()
        if user:
            bookmarks = Bookmark.objects.filter(user=user).values_list('post', flat=True)
            return Post.objects.filter(id__in=bookmarks)
        return Post.objects.none()