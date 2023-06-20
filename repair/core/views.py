from rest_framework.viewsets import ModelViewSet

from core.models import ServiceMan, Order
from core.serializers import ServicemanModelSerializer, OrderModelSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer


class ServicemanViewSet(ModelViewSet):
    queryset = ServiceMan.objects.all()
    serializer_class = ServicemanModelSerializer

