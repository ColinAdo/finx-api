from rest_framework.routers import DefaultRouter

from .views import CommentViewset

route = DefaultRouter()
route.register(r'comment', CommentViewset, basename='comments')
urlpatterns = route.urls