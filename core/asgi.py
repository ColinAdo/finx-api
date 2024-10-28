import os

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from django.urls import path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

django_asgi_app = get_asgi_application()

from chats.middleware.jwt_auth_middleware import JWTAuthMiddleware
from chats.consumers import ThumbnailConsumer, ChatConsumer


application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        JWTAuthMiddleware(
            URLRouter([
                path('api/v1/chat/', ThumbnailConsumer.as_asgi()),
                path('api/v1/chat/<str:room_name>/', ChatConsumer.as_asgi()),
            ])
        )
    ),
})