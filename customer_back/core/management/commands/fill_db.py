import random

from django.core.management.base import BaseCommand
from phonenumber_field.phonenumber import PhoneNumber
from django.conf import settings

from core.models import Client, Order


def get_new_client(username: str):
    client = Client.objects.get_or_create(
        username=f"{username}@email.ru",
        defaults=dict(
            password=123,
            last_name=random.choice(
                ["Иванов", "Петров", "Сидоров", "Пупкин", "Лапушкин"]
            ),
            first_name=random.choice(
                ["Евгений", "Олег", "Александр", "Егор", "Владимир"]
            ),
            patronymic=random.choice(
                ["Иванович", "Петрович", "Сидорович", "Егорович", "Олегович"]
            ),
            address=get_address(),
            email=f"{username}@email.ru",
            phone_number=PhoneNumber.from_string(
                str(random.randint(89210000000, 89219999999)),
                region=settings.PHONE_NUMBER_REGION,
            ),
        ),
    )[0]
    client.set_password(username)
    client.save()
    return client


def get_new_order(
    client,
):
    return Order.objects.get_or_create(
        client=client,
        defaults=dict(
            client=client,
            status=random.choice([status for status in Order.StatusEnum]),
            serviceman_description="Вскрыл корпус молотком, все хорошо!",
            customer_description="Чета экран не работает",
            deliveryman_description="Опять в Мухосранске, ну емае",
            category=random.choice([status for status in Order.GadgetType.TELEPHONE]),
        ),
    )[0]


def get_address():
    cities = ["Санкт-Петербург", "Омск"]
    streets = ["Строителей", "Обводный канал", "Архитекторов", "Уточкина"]
    houses = range(200)
    appartments = range(200)
    return f"г. {random.choice(cities)} ул. {random.choice(streets)} д. {random.choice(houses)} кв. {random.choice(appartments)}"


class Command(BaseCommand):
    def handle(self, *args, **options):
        for num in range(30):
            get_new_order(client=get_new_client(f"client{num}"))
