from django.urls import path

from .views import UserFollowView

urlpatterns = [
    path('follow/<int:pk>/', UserFollowView.as_view(), name='follow-unfollow'),
]