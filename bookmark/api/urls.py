from django.urls import path

from .views import BookmarkView

urlpatterns = [
    path('bookmark/<int:pk>/', BookmarkView.as_view(), name='save'),
]