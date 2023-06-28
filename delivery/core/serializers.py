from rest_framework import serializers

from core.models import Order, Address, City

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [
            "id",
            "name"
        ]

class AddresSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    class Meta:
        model = Address
        fields = [
            "id",
            "city",
            "street",
            "building",
            "apartment"
        ]

class OrderSerializer(serializers.ModelSerializer):
    address = AddresSerializer()
    class Meta:
        model = Order
        fields = [
            "id",
            "phone_number",
            "status",
            "address",
            "deliveryman",
            "created",
            "updated"
        ]
