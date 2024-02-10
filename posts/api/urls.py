from django.urls import path

from .views import (
    PostListCreateView, 
    PostDetailView, 
    CommentListCreateView,
    CommentDetailView,
)

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/comments/',  CommentListCreateView.as_view(), name='comments'),
    path('posts/<int:pk>/comments/<int:comment_pk>/',
         CommentDetailView.as_view(), name='comment-detail'),
]