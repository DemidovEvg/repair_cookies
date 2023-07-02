from rest_framework.serializers import ModelSerializer

from core.models import Client, Order, Category


class ClientModelSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "id",
            "phone_number",
            "address"
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
        )


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name"

        )


class OrderModelSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "client",
            "category",
            "comments",
            "status",
            "created",
            "updated",
            "deleted",
        )

