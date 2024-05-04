from rest_framework.routers import DefaultRouter

from .views import ProfileViewset

routes = DefaultRouter()
routes.register(r'profile', ProfileViewset)
urlpatterns = routes.urls