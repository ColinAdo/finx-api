from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    PostviewSet,

    CommentListCreateView,
    CommentDetailView,
)

urlpatterns = [
    path('posts/<int:pk>/comments/',
         CommentListCreateView.as_view(), name='comments'),
    path('posts/<int:pk>/comments/<int:comment_pk>/',
         CommentDetailView.as_view(), name='comment-detail'),
]

router = SimpleRouter()
router.register('posts', PostviewSet, basename='posts')

urlpatterns += router.urls
