from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient

from core.models import TokenData, Client, Order
from core.serializers import (
    ClientModelSerializer,
    NewClientModelSerializer,
    OrderModelSerializer,
)

client = APIClient()

User = get_user_model()
# Create your tests here.

"""тестирование создания пользователя и заказа"""


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
        order = Order.objects.create(client=client, status="CREATED",
                                     category="TELEPHONE")
        self.assertEqual(order.client, client)
        self.assertEqual(order.status, "CREATED")
        self.assertEqual(order.category, "TELEPHONE")


"""тестирование представления заказа и клиента"""


class OrderViewSetTestCase(TestCase):
    def setUp(self):
        self.order = Order.objects.create(
            client=Client.objects.create(username="testuser", password="password"),
            status="CREATED", category="TELEPHONE")

    def test_order_list(self):
        url = reverse("order-list")
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_order_detail(self):
        url = reverse("order-detail", args=[self.order.id])
        response = client.get(url)
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


"""тестирование сериализатора заказа и клиента"""


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

