from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.routing import get_default_application

from chats.middleware.jwt_auth_middleware import JWTAuthMiddleware
from chats import routing

# django_asgi_app = get_asgi_application()
django_asgi_app = get_default_application()


application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AllowedHostsOriginValidator(
        JWTAuthMiddleware(  
            URLRouter(
                routing.websocket_urlpatterns
            )
        )
    ),
})

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AllowedHostsOriginValidator(
        JWTAuthMiddleware(
            URLRouter(routing.websocket_urlpatterns)
        )
    ),
})