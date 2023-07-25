from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.shortcuts import render

from core.models import Client, Order, Price
from core.serializers import (
    ClientModelSerializer,
    OrderModelSerializer,
    NewClientModelSerializer,
    PriceSerializer,
)


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer

    def get_queryset(self):
        email = self.request.query_params.get("email")
        if email:
            return self.queryset.filter(client__email=email)
        return self.queryset

    def perform_update(self, serializer):
        instance = serializer.save()
        OrderModelSerializer.create_or_update_outer_order(instance)

    def perform_create(self, serializer):
        instance = serializer.save()
        OrderModelSerializer.create_or_update_outer_order(instance)

    @action(methods=["patch"], detail=True, url_path="sync", url_name="sync_update")
    def action_sync_update(self, request, *args, **kwargs):
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
