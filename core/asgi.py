import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
import chats.routing
from chats.middleware.jwt_auth_middleware import JWTAuthMiddleware  # Import your custom middleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

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
