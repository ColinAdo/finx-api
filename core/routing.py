from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

from chats.middleware.jwt_auth_middleware import JWTAuthMiddleware
import chats.routing


application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        JWTAuthMiddleware(  
            URLRouter(
                chats.routing.websocket_urlpatterns
            )
        )
    ),
})