from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action


from accounts.api.serializers import UserSerializer

from posts.models import Post
from posts.api.serializers import PostSerializer

from social.models import UserFollow
from social.api.serializers import UserFollowSerializer

from .permissions import IsOwnerOrReadOnly

# User views
User = get_user_model()

class ProfileViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user, context={'request': request}) 

        posts = Post.objects.filter(author=request.user)
        following = UserFollow.objects.filter(follows=request.user)
        followers = UserFollow.objects.filter(user=request.user)

        serialized_post = PostSerializer(posts, many=True, context={'request': request})
        serialized_following = UserFollowSerializer(following, many=True, context={'request': request})
        serialized_followers = UserFollowSerializer(followers, many=True, context={'request': request})

        data = {
            'profile': serializer.data,
            'posts': serialized_post.data,
            'following': serialized_followers.data,
            'following_count': len(serialized_followers.data),
            'followers': serialized_following.data,
            'followers_count': len(serialized_following.data),
        }

        return Response(data)

