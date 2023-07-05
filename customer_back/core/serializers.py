from rest_framework.serializers import ModelSerializer

from core.models import Client, Order


class ClientModelSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "id",
            "phone_number",
            "address",
            "username",
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


class OrderModelSerializer(ModelSerializer):
    client = ClientModelSerializer()

    class Meta:
        model = Order
        fields = (
            "id",
            "client",
            "category",
            "serviceman_description",
            "customer_description",
            "deliveryman_description",
            "status",
            "created",
            "updated",
            "deleted",
        )

    def create(self, validated_data):
        self.create_or_update_client(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        self.create_or_update_client(validated_data)
        return super().update(instance, validated_data)

    def create_or_update_client(self, validated_data):
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
