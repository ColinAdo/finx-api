from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('api/v1/chat/', consumers.ThumbnailConsumer.as_asgi()),
    path('api/v1/chat/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]
