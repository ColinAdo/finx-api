from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("chat/", include("chats.urls")),
    path('admin/', admin.site.urls),
    path('api/', include('djoser.urls')),
    path('api/', include('accounts.urls')),
    path('api/v1/', include('accounts.api.urls')),
    path('api/', include('profiles.api.urls')),
    path('api/', include('posts.api.urls')),
    path('api/', include('comments.api.urls')),
    path('api/', include('likes.api.urls')),
    path('api/', include('social.api.urls')),
    path('api/', include('chats.api.urls')),
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
