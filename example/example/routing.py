from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django_private_chat3 import urls

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            urls.websocket_urlpatterns
        )
    ),
})
