from django.urls import path

from .views import LikePostView

urlpatterns = [
    path('like/<int:pk>/', LikePostView.as_view(), name='like'),
]