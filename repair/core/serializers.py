from rest_framework.serializers import ModelSerializer

from core.models import ServiceMan, Order, Price


class PriceModelSerializer(ModelSerializer):
    class Meta:
        model = Price
        fields = "__all__"


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
            "model",
            "category",
            "repair_lvl",
            "amount_due_by",
            "created",
        ]
