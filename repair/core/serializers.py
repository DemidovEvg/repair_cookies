from core.models import Order, ServiceMan
from rest_framework.serializers import ModelSerializer


class ServicemanModelSerializer(ModelSerializer):
    class Meta:
        model = ServiceMan
        fields = "__all__"


class OrderModelSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "category",
            "serviceman",
            "serviceman_description",
            "customer_description",
            "deliveryman_description",
            "amount_due_by",
            "created",
        ]
