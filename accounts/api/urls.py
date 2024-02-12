from django.urls import path

from .views import UserListView, UserApiDetailView

urlpatterns = [
    path("users/", UserListView.as_view(), name="users"),
    path("users/<int:pk>/", UserApiDetailView.as_view(), name="users"),
]