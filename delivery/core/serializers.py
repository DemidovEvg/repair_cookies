from core.models import Address, City, Client, Order
from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["id", "name"]


class AddresSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Address
        fields = ["id", "city", "street", "building", "apartment"]


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
            "first_name",
            "patronymic",
            "last_name",
            "phone_number",
            "email",
        ]
        extra_kwargs = {
            "id": {"validators": []},
            "phone_number": {"validators": []},
        }

    def validate(self, attrs):
        return super().validate(attrs)


class OrderSerializer(serializers.ModelSerializer):
    address = serializers.StringRelatedField()
    client = ClientSerializer()

    class Meta:
        model = Order
        fields = [
            "id",
            "client",
            "status",
            "category",
            "address",
            "serviceman_description",
            "customer_description",
            "deliveryman_description",
            "payment_completed",
            "amount_due_by",
            "created",
        ]

    def create(self, validated_data):
        self.create_or_update_client(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        self.create_or_update_client(validated_data)
        return super().update(instance, validated_data)

    def create_or_update_client(self, validated_data):
        if "client" in validated_data:
            client_instance = Client.objects.filter(id=validated_data["client"]["id"]).first()
            client_serializer = ClientSerializer(instance=client_instance, data=validated_data["client"], partial=True)
            client_serializer.is_valid(raise_exception=True)
            client_instance = client_serializer.save()
            validated_data["client"] = client_instance
