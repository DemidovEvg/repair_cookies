from rest_framework.viewsets import ModelViewSet

from core.models import CustomUser, Order
from core.serializers import CustomUserModelSerializer, OrderModelSerializer


# Create your views here.
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer


class OrderSnakeCaseViewSet(OrderViewSet):
    parser_classes = ("rest_framework.parsers.JSONParser",)
    renderer_classes = ("rest_framework.renderers.JSONRenderer",)


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer


class CustomUserSnakeCaseViewSet(CustomUserViewSet):
    parser_classes = ("rest_framework.parsers.JSONParser",)
    renderer_classes = ("rest_framework.renderers.JSONRenderer",)
