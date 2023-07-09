from core.models import Client, Order
from core.serializers import ClientModelSerializer, OrderModelSerializer
from rest_framework.viewsets import ModelViewSet


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientModelSerializer
