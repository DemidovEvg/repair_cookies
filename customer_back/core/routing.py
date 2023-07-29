from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path("ws/client-orders/<str:email>/", consumers.ClientConsumer.as_asgi()),
]
