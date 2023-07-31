from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import APIException
from django.contrib.auth.hashers import make_password
from django.conf import settings
from requests.exceptions import ConnectionError

from core.models import Client, Order, Price, RepairKind
from core.services.order_service import create_or_update

from rest_framework import serializers
import re
from core.not_word_mat import search_word_mat


class ClientModelSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "id",
            "phone_number",
            "address",
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

    def validate(self, data):
        my_str = data['last_name']
        if len(my_str) > 0:
            if not bool(re.match('^[А-яа-я0-9 -]+$', my_str)):
                raise serializers.ValidationError('Можно вводить только русские буквы, тире и пробел, строка: ' + my_str)
            if search_word_mat(my_str):
                raise serializers.ValidationError(
                    'Вы ввели нецензурное слово в поле: ФАМИЛИЯ. Если не согласны пишите на email: info@смартремонт.рф')

        my_str1 = data['first_name']
        if not bool(re.match('^[А-яа-я0-9 -]+$', my_str1)):
            raise serializers.ValidationError('Можно вводить только русские буквы, тире и пробел, строка: ' + my_str1)
        if search_word_mat(my_str1):
            raise serializers.ValidationError(
                'Вы ввели нецензурное слово в поле: ИМЯ. Если не согласны пишите на email: info@смартремонт.рф')

        my_str2 = data['patronymic']
        if len(my_str2) > 0:
            if not bool(re.match('^[А-яа-я0-9 -]+$', my_str2)):
                raise serializers.ValidationError('Можно вводить только русские буквы, тире и пробел, строка: ' + my_str2)
            if search_word_mat(my_str2):
                raise serializers.ValidationError(
                    'Вы ввели нецензурное слово в поле: ОТЧЕСТВО. Если не согласны пишите на email: info@смартремонт.рф')

        return data

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

    def create(self, validated_data):
        self.create_or_update_client(validated_data)
        instance = super().create(validated_data)
        return instance

    def update(self, instance, validated_data):
        self.create_or_update_client(validated_data)
        instance = super().update(instance, validated_data)
        return instance

    @staticmethod
    def create_or_update_client(validated_data):
        if "client" in validated_data:
            client_instance = Client.objects.filter(
                id=validated_data["client"]["id"]
            ).first()
            print(1111111111111)
            print(client_instance)
            client_serializer = ClientModelSerializer(
                instance=client_instance, data=validated_data["client"], partial=True
            )
            client_serializer.is_valid(raise_exception=True)
            client_instance = client_serializer.save()
            validated_data["client"] = client_instance

    @classmethod
    def create_or_update_outer_order(cls, order: Order):
        exceptions = []
        try:
            service_create = f"{settings.DELIVERY_SERVICE}/api/orders/"
            service_update = f"{service_create}{order.id}/"
            data = cls(instance=order).data

            create_or_update(service_create, service_update, data)
        except ConnectionError as exc:
            exceptions.append(exc)

        try:
            service_create = f"{settings.REPAIR_SERVICE}/api/orders/"
            service_update = f"{service_create}{order.id}/"
            create_or_update(service_create, service_update, data)
        except ConnectionError as exc:
            exceptions.append(exc)

        if exceptions:
            raise APIException(
                "Не получилось отправить заказ в службу доставки, "
                "пожалуйста обратитесь в службу поддержки!"
            )


class RepairKindSerializer(ModelSerializer):
    class Meta:
        model = RepairKind
        fields = (
            "id",
            "name",
        )


class PriceSerializer(ModelSerializer):
    repair_kind = RepairKindSerializer()
    repair_subkind = RepairKindSerializer()

    class Meta:
        model = Price
        fields = (
            "id",
            "equipment_category",
            "repair_kind",
            "repair_subkind",
            "name",
            "value",
        )
