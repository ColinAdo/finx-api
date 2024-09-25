from rest_framework.routers import DefaultRouter

from .views import ProfileViewset, UsersProfileViewset

routes = DefaultRouter()
routes.register(r'profile', ProfileViewset)
routes.register(r'users', UsersProfileViewset)
urlpatterns = routes.urls