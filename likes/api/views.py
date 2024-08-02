from django.core.exceptions import ObjectDoesNotExist

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .serializers import LikeSerializer
from posts.models import Post
from likes.models import LikePost

# Like post view
class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LikeSerializer

    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            like_post = LikePost.objects.filter(post=post)

            serializer = LikeSerializer(like_post, many=True)
            return Response({"success": True, "like_post": serializer.data})

        except ObjectDoesNotExist:
            return Response({"success": False, "message": "post does not exist"})
        
    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            new_like_post = LikePost.objects.get_or_create(user=request.user, post=post)

            if not new_like_post[1]:
                new_like_post[0].delete()
                return Response({"success": True, "message": "post unliked"})
            else:
                return Response({"success": True, "message": "post liked"})
            
        except ObjectDoesNotExist:
            return Response({ "success": False, "message": "post does not exist" })
