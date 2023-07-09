import random
from uuid import uuid4

from core.models import Address, City, Client, Deliveryman, DeliveryUser, Order
from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError


def get_delivery_group():
    deliveries_group, created = Group.objects.get_or_create(name="Доставщики")

    def get_perm(name):
        return Permission.objects.get(codename=name)

    deliveries_group.permissions.add(
        get_perm("add_address"),
        get_perm("change_address"),
        get_perm("delete_address"),
        get_perm("view_address"),
        get_perm("add_city"),
        get_perm("change_city"),
        get_perm("delete_city"),
        get_perm("view_city"),
        get_perm("add_order"),
        get_perm("change_order"),
        get_perm("delete_order"),
        get_perm("view_order"),
    )
    return deliveries_group


def get_random_string(arr):
    return


def get_new_deliveryman(username: str, is_team_lead: bool = False):
    try:
        user = DeliveryUser.objects.create_user(
            last_name=random.choice(["Иванов", "Петров", "Сидоров", "Пупкин", "Лапушкин"]),
            first_name=random.choice(["Евгений", "Олег", "Александр", "Егор", "Владимир"]),
            patronymic=random.choice(["Ивинович", "Петрович", "Сидорович", "Егорович", "Олегович"]),
            username=username,
            email=f"{username}@email.ru",
            password=username,
            is_staff=True,
        )
    except IntegrityError:
        user = DeliveryUser.objects.get(username=username)
    deliveries_group = get_delivery_group()
    deliveries_group.user_set.add(user)
    return Deliveryman.objects.get_or_create(user=user, is_team_lead=is_team_lead)[0]


def get_new_client(username: str):
    client = Client.objects.get_or_create(
        last_name=random.choice(["Иванов", "Петров", "Сидоров", "Пупкин", "Лапушкин"]),
        first_name=random.choice(["Евгений", "Олег", "Александр", "Егор", "Владимир"]),
        patronymic=random.choice(["Ивинович", "Петрович", "Сидорович", "Егорович", "Олегович"]),
        email=f"{username}@email.ru",
        defaults=dict(phone_number=str(random.randint(80000000000, 89999999999))),
    )[0]
    return client


def get_new_order(
    client,
    deliveryman: Deliveryman | None = None,
    address: str | None = None,
):
    return Order.objects.create(
        id=uuid4().hex,
        client=client,
        address=address,
        deliveryman=deliveryman,
        serviceman_description="Вскрыл корпус молотком, все хорошо!",
        customer_description="Чета экран не работает",
        deliveryman_description="Опять в Мухосранске, ну емае",
        category=Order.GadgetType.TELEPHONE,
    )


class Command(BaseCommand):
    def handle(self, *args, **options):
        habarovsk = City.objects.create(name="Хабаровск")
        address1 = Address.objects.create(city=habarovsk, street="Строителей", building="60а", apartment=49)
        address2 = Address.objects.create(city=habarovsk, street="Ленина", building="56", apartment=123)

        deliveryman1 = get_new_deliveryman("deliveryman1")
        deliveryman2 = get_new_deliveryman("deliveryman2")
        deliveryman_team_lead = get_new_deliveryman("deliveryman_team_lead", True)

        get_new_order(client=get_new_client("client1"), deliveryman=deliveryman1, address=address1)
        get_new_order(client=get_new_client("client2"), deliveryman=deliveryman1)
        get_new_order(client=get_new_client("client3"), deliveryman=deliveryman1)
        get_new_order(client=get_new_client("client4"), deliveryman=deliveryman2, address=address2)
        get_new_order(client=get_new_client("client5"))
        get_new_order(client=get_new_client("client6"))
