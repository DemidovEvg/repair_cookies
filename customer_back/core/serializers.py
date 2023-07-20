from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from django.conf import settings
from core.services.order_service import create_or_update

from core.models import Client, Order


class ClientModelSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "id",
            "phone_number",
            "address",
            "email",
            "first_name",
            "patronymic",
            "last_name",
            "is_active",
        )
        extra_kwargs = {
            "id": {"validators": []},
            "phone_number": {"validators": []},
        }


class NewClientModelSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "phone_number",
            "email",
            "password",
            "first_name",
            "patronymic",
            "last_name",
        )

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        validated_data["username"] = validated_data["email"]
        return super().create(validated_data)


class OrderModelSerializer(ModelSerializer):
    client = ClientModelSerializer()

    class Meta:
        model = Order
        fields = (
            "id",
            "client",
            "category",
            "model",
            "serviceman_description",
            "customer_description",
            "deliveryman_description",
            "status",
            "created",
            "updated",
            "deleted",
        )

    def create_or_update_outer_order(self, order: Order):
        exceptions = []
        try:
            service_create = f"{settings.DELIVERY_SERVICE}/api/orders/"
            service_update = f"{service_create}{order.id}/"
            data = OrderModelSerializer(instance=order).data

            create_or_update(service_create, service_update, data)
        except Exception as exc:
            exceptions.append(exc)

        try:
            service_create = f"{settings.REPAIR_SERVICE}/api/orders/"
            service_update = f"{service_create}{order.id}/"
            create_or_update(service_create, service_update, data)
        except Exception as exc:
            exceptions.append(exc)

        if exceptions:
            raise Exception(repr(exceptions))

    @staticmethod
    def create_or_update_client(validated_data):
        if "client" in validated_data:
            client_instance = Client.objects.filter(
                id=validated_data["client"]["id"]
            ).first()
            client_serializer = ClientModelSerializer(
                instance=client_instance, data=validated_data["client"], partial=True
            )
            client_serializer.is_valid(raise_exception=True)
            client_instance = client_serializer.save()
            validated_data["client"] = client_instance
