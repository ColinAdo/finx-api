from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import PostviewSet

router = DefaultRouter()
router.register(r'posts', PostviewSet, basename='posts')

urlpatterns = router.urls
