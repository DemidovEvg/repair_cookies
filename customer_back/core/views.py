from rest_framework.viewsets import ModelViewSet

from core.models import Client, Order
from core.serializers import ClientModelSerializer, OrderModelSerializer


# Create your views here.
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientModelSerializer
