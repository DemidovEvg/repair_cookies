from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from core.models import Order
from core.serializers import OrderModelSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderModelSerializer
