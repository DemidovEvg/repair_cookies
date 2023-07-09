from core.models import Order
from core.serializers import OrderSerializer
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderSerializer
