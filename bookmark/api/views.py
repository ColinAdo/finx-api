from django.core.exceptions import ObjectDoesNotExist

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .serializer import BookmarkSerializer
from posts.models import Post
from bookmark.models import Bookmark

# Bookmark post view
class BookmarkView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookmarkSerializer

    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            bookmark_post = Bookmark.objects.filter(post=post)

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
