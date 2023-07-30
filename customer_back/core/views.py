import logging

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.shortcuts import render
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from core.models import Client, Order, Price
from core.serializers import (
    ClientModelSerializer,
    OrderModelSerializer,
    NewClientModelSerializer,
    PriceSerializer,
)

logger = logging.getLogger(__name__)


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer

    def __init__(self, *args, **kwargs):
        self.need_create_or_update_outer_order = True
        super().__init__(*args, **kwargs)

    def get_queryset(self):
        email = self.request.query_params.get("email")
        if email:
            return self.queryset.filter(client__email=email)
        return self.queryset

    def perform_update(self, serializer):
        instance = serializer.save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"sync_client_orders_channel_group_{instance.client_id.hex}",
            {
                "type": "websocket.receive",
                "text": f"update_order order_id={instance.id.hex}",
            },
        )
        if self.need_create_or_update_outer_order:
            OrderModelSerializer.create_or_update_outer_order(instance)

    def perform_create(self, serializer):
        instance = serializer.save()
        if self.need_create_or_update_outer_order:
            try:
                OrderModelSerializer.create_or_update_outer_order(instance)
            except Exception as exc:
                logger.exception(repr(exc))
                raise

    @action(methods=["patch"], detail=True, url_path="sync", url_name="sync_update")
    def action_sync_update(self, request, *args, **kwargs):
        self.need_create_or_update_outer_order = False
        return super().update(request, *args, **kwargs)


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return NewClientModelSerializer
        return ClientModelSerializer

    def get_queryset(self):
        email = self.request.query_params.get("email")
        if email:
            return Client.objects.filter(email=email)
        return self.queryset


class PriceViewSet(ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


def client_orders(request, email):
    return render(request, "core/client_orders.html", {"email": email})
