from rest_framework.viewsets import ModelViewSet

from core.models import Client, Order, Category
from core.serializers import ClientModelSerializer, OrderModelSerializer, CategoryModelSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientModelSerializer


