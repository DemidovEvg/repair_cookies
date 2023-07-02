from rest_framework.serializers import ModelSerializer

from core.models import ServiceMan, Order


class ServicemanModelSerializer(ModelSerializer):
    class Meta:
        model = ServiceMan
        fields = "__all__"


class OrderModelSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ("__all__")
