from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

from chats.middleware.jwt_auth_middleware import JWTAuthMiddleware
import chats.routing

django_asgi_app = get_asgi_application()


application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AllowedHostsOriginValidator(
        JWTAuthMiddleware(  
            URLRouter(
                chats.routing.websocket_urlpatterns
            )
        )
    ),
})