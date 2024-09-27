from django.urls import path

from .views import UserFollowView

urlpatterns = [
    path('connect/<int:pk>/', UserFollowView.as_view(), name='follow-unfollow'),
]