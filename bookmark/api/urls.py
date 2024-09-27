from django.urls import path

from .views import BookmarkView, BookmarkedPostsView

urlpatterns = [
    path('bookmark/<int:pk>/', BookmarkView.as_view(), name='save'),
     path('bookmarked/<str:username>/posts/', BookmarkedPostsView.as_view(), name='bookmarked-posts'),
]