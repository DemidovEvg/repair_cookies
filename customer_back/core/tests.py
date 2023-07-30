from django.test import TestCase, RequestFactory
import unittest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient, APIRequestFactory

from .models import Client, TokenData, Order, RepairKind, Price
from .views import PriceViewSet, OrderViewSet
from .serializers import (
    ClientModelSerializer,
    NewClientModelSerializer,
    OrderModelSerializer,
    PriceSerializer,
)

client = APIClient()

User = get_user_model()
# Create your tests here.

"""тестирование моделей пользователя, заказа, прайса"""


class AbstractUserTest(TestCase):
    def test_create_user(self):
        pass


class ClientModelTestCase(TestCase):
    def test_client_model_creation(self):
        client = Client.objects.create(username="testuser", password="password")
        self.assertEqual(client.username, "testuser")
        self.assertFalse(client.check_password("password"))


class TokenDataModelTestCase(TestCase):
    def test_token_data_model_creation(self):
        user = User.objects.create(username="testuser", password="password")
        token_data = TokenData.objects.create(user=user, token="token")
        self.assertEqual(token_data.user, user)
        self.assertEqual(token_data.token, "token")


class OrderModelTestCase(TestCase):
    def test_order_model_creation(self):
        client = Client.objects.create(username="testuser", password="password")
        order = Order.objects.create(
            client=client, status="CREATED", category="TELEPHONE"
        )
        self.assertEqual(order.client, client)
        self.assertEqual(order.status, "CREATED")
        self.assertEqual(order.category, "TELEPHONE")


class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", email="testuser@example.com", password="testpassword"
        )
        self.repair_kind = RepairKind.objects.create(name="Test Repair Kind")
        self.price = Price.objects.create(
            equipment_category=Price.GadgetType.TELEPHONE,
            repair_kind=self.repair_kind,
            repair_subkind=self.repair_kind,
            name="Test Repair",
            value=10.0,
        )

    def test_repair_kind_model(self):
        self.assertEqual(self.repair_kind.name, "Test Repair Kind")

    def test_price_model(self):
        self.assertEqual(self.price.equipment_category, Price.GadgetType.TELEPHONE)
        self.assertEqual(self.price.repair_kind, self.repair_kind)
        self.assertEqual(self.price.repair_subkind, self.repair_kind)
        self.assertEqual(self.price.name, "Test Repair")
        self.assertEqual(self.price.value, 10.0)


"""тестирование представления заказа, клиента, прайса"""


class OrderViewSetTest(unittest.TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = OrderViewSet.as_view({"get": "list"})

    def test_get_queryset_with_email(self):
        request = self.factory.get("/orders/", {"email": "test@example.com"})
        response = self.view(request)
        self.assertEqual(response.status_code, 200)

    def test_get_queryset_without_email(self):
        request = self.factory.get("/orders/")
        response = self.view(request)
        self.assertEqual(response.status_code, 200)


class ClientViewSetTestCase(TestCase):
    def setUp(self):
        self.client = Client.objects.create(username="testuser", password="password")

    def test_client_list(self):
        url = reverse("client-list")
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_client_detail(self):
        url = reverse("client-detail", args=[self.client.id])
        response = client.get(url)
        self.assertEqual(response.status_code, 200)


class PriceViewSetTest(unittest.TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = PriceViewSet.as_view({"get": "list"})

    def test_get_queryset_with_category(self):
        request = self.factory.get("/prices/", {"category": "electronics"})
        response = self.view(request)
        self.assertEqual(response.status_code, 200)

    def test_get_queryset_without_category(self):
        request = self.factory.get("/prices/")
        response = self.view(request)
        self.assertEqual(response.status_code, 200)


"""тестирование сериализатора заказа, клиента, прайса"""


class ClientModelSerializerTestCase(TestCase):
    def test_client_model_serializer(self):
        client_data = {
            "id": 1,
            "phone_number": "123456789",
            "address": "123 Street",
            "email": "test@example.com",
            "first_name": "Биба",
            "patronymic": "Боба",
            "last_name": "Даблдолб",
            "is_active": True,
        }
        serializer = ClientModelSerializer(data=client_data)
        self.assertTrue(serializer.is_valid())


class NewClientModelSerializerTestCase(TestCase):
    def test_new_client_model_serializer(self):
        client_data = {
            "phone_number": "123456789",
            "email": "test@example.com",
            "password": "password",
            "first_name": "Биба",
            "patronymic": "Боба",
            "last_name": "Даблдолб",
        }
        serializer = NewClientModelSerializer(data=client_data)
        self.assertFalse(serializer.is_valid())


class OrderModelSerializerTestCase(TestCase):
    def setUp(self):
        self.client = Client.objects.create(username="testuser", password="password")
        self.order_data = {
            "id": 1,
            "client": {
                "id": self.client.id,
                "phone_number": "123456789",
                "address": "123 Street",
                "email": "test@example.com",
                "first_name": "John",
                "patronymic": "Doe",
                "last_name": "Smith",
                "is_active": True,
            },
            "category": "TELEPHONE",
            "model": "iPhone",
            "serviceman_description": "Some description",
            "customer_description": "Some description",
            "deliveryman_description": "Some description",
            "status": "CREATED",
        }

    def test_order_model_serializer(self):
        serializer = OrderModelSerializer(data=self.order_data)
        self.assertTrue(serializer.is_valid())


class PriceSerializerTest(unittest.TestCase):
    def test_valid_data(self):
        data = {
            "id": 1,
            "equipment_category": "Electronics",
            "repair_kind": {"id": 1, "name": "Screen Replacement"},
            "repair_subkind": {"id": 1, "name": "iPhone"},
            "name": "Screen Replacement for iPhone",
            "value": 100.00,
        }
        serializer = PriceSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_data(self):
        data = {
            "id": 1,
            "equipment_category": "Electronics",
            "repair_kind": {"id": 1, "name": "Screen Replacement"},
            "repair_subkind": {"id": 1, "name": "iPhone"},
            "name": "Screen Replacement for iPhone",
            "value": "Invalid Value",
        }
        serializer = PriceSerializer(data=data)
        self.assertFalse(serializer.is_valid())
