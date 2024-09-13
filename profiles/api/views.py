from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from .serializers import ProfileSerializers
from .permissions import IsOwnerOrReadOnly

from profiles.models import Profile

from posts.api.serializers import PostSerializer
from posts.models import Post

from social.models import UserFollow
from social.api.serializers import UserFollowSerializer

# Profile viewset
class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        profile = Profile.objects.get(owner=request.user)
        serializer = ProfileSerializers(profile, context={'request': request})

        posts = Post.objects.filter(author=request.user)
        following = UserFollow.objects.filter(follows=request.user)
        followers = UserFollow.objects.filter(user=request.user)

        serialized_post = PostSerializer(posts, many=True)
        serialized_following = UserFollowSerializer(following, many=True)
        serialized_followers = UserFollowSerializer(followers, many=True)

        data = {
            'profile': serializer.data,
            'posts': serialized_post.data,
            'following': serialized_followers.data,
            'following_count': len(serialized_followers.data),
            'followers': serialized_following.data,
            'followers_count': len(serialized_following.data),
        }

        return Response(data)

