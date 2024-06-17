from rest_framework import viewsets, permissions
from rest_framework.response import Response

from profiles.models import Profile
from .serializers import ProfileSerializers
from .permissions import IsOwnerOrReadOnly
from posts.api.serializers import PostSerializer
from posts.models import Post

# Profile viewset
class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def retrieve(self, request, pk, *args, **kwargs):
        try:
            user = request.user
            posts = Post.objects.filter(author=user)
            profile = Profile.objects.get(id=pk)
            
            serialized_post = PostSerializer(posts, many=True)
            serialized_profile = ProfileSerializers(profile)

            data = {
                "profile": serialized_profile.data,
                "posts": serialized_post.data
            }
        except:
            return Response({"Message": "User profile does not exist..."})


        return Response(data)


