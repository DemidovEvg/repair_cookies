from rest_framework.viewsets import ModelViewSet

from core.models import Client, Order
from core.serializers import ClientModelSerializer, OrderModelSerializer, NewClientModelSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer

    def get_queryset(self):
        email = self.request.query_params.get('email')
        if email:
            return Order.objects.filter(client__email=email)
        return self.queryset


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return NewClientModelSerializer
        return ClientModelSerializer

    def get_queryset(self):
        email = self.request.query_params.get('email')
        if email:
            return Client.objects.filter(email=email)
        return self.queryset
