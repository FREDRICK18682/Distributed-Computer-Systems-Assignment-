"""
ASGI config for node_chart project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import Chart_Room

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Distributed_chart_application.settings')

application = ProtocolTypeRouter({
    "http":get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            Chart_Room.routing.websocket_urlpatterns
        ),
    ),
})
