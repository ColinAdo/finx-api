from rest_framework.routers import DefaultRouter

from .views import ConversationViewSet

routes = DefaultRouter()
routes.register(r'conversations', ConversationViewSet, basename='conversations')
urlpatterns = routes.urls