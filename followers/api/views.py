from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from core.authentications import CustomJWTAuthentication

from followers.models import UserFollow
from .serializers import UserFollowSerializer


class UserFollowView(APIView):
    queryset = UserFollow.objects.all()
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserFollowSerializer

    def get(self, request, pk):
        User = get_user_model()
        user = User.objects.get(pk=pk)
        following = UserFollow.objects.filter(user=user)
        followers = UserFollow.objects.filter(follows=user)

        following_serializer = UserFollowSerializer(following, many=True)
        followers_serializer = UserFollowSerializer(followers, many=True)

        following_count = len(following_serializer.data)
        followers_count = len(followers_serializer.data)

        return Response(
            {
                "success": True, 
                "following": following_serializer.data, 
                "following_count": following_count,
                "followers": followers_serializer.data,
                "followers_count": followers_count,

            })

        
    def post(self, request, pk):
        try:
            User = get_user_model()
            following = User.objects.get(id=pk)
            follower = UserFollow.objects.get_or_create(user=request.user, follows=following)

            if not follower[1]:
                follower[0].delete()
                return Response({"success": True, "message": f"You unfollowed {following.username}"})
            
            else:
                return Response({"success": True, "message": f"You followed {following.username}"})

        except ObjectDoesNotExist:
            return Response({"success": False, "message": "following user does not exist"})
    

