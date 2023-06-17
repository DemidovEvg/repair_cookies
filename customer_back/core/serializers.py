from rest_framework.serializers import ModelSerializer

from core.models import Client, Order


class ClientModelSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "id",
            "phone_number",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
        )


class OrderModelSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "client",
            "status",
            "created",
            "updated",
            "deleted",
        )
