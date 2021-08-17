"""
ASGI config for question_test_site project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from api.middlewares import TokenAuthMiddleware
from api.routing import ws_urlpatterns
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'question_test_site.settings')

# application = get_asgi_application()
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(URLRouter(ws_urlpatterns)),
})
