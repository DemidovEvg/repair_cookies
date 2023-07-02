from uuid import uuid4

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from customer.settings import PHONE_NUMBER_REGION


# Create your models here.


class Client(AbstractUser):
    id = models.UUIDField(verbose_name="Идентификатор", default=uuid4, primary_key=True)
    address = models.TextField("Адрес клиента", default='')
    location = models.CharField(max_length=30, blank=True)
    phone_number = PhoneNumberField(
        "Номер телефона клиента",
        unique=True, region=PHONE_NUMBER_REGION, max_length=12
    )


class TokenData(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        unique=True,
        related_name="token_data",
    )
    token = models.CharField(verbose_name="Токен", max_length=1500)


class Category(models.Model):
    """Вид техники"""

    class GadgetType(models.TextChoices):
        TELEPHONE = ("telephone", "телефон")
        LAPTOP = ("laptop", "ноутбук")
        TABLET = ("tablet", "планшет")

    name = models.CharField("Категория Техники", max_length=250, default='')

    class Meta:
        verbose_name = "Гаджет"
        verbose_name_plural = "Гаджеты"


class Order(models.Model):
    class StatusEnum(models.TextChoices):
        CREATED = ("CREATED", "Заказ создан")
        APPOINTED = ("APPOINTED", "Заказ принят")
        IN_WORK = ("IN_WORK", "Заказ в работе")
        DONE = ("DONE", "Заказ выполнен")

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(
        verbose_name="Статус заказа",
        max_length=12,
        choices=StatusEnum.choices,
        default=StatusEnum.CREATED,
    )
    name = models.SlugField("Техника", max_length=200,
                            choices=Category.GadgetType.choices, null=True)
    comments = models.TextField("Комментарий к заказу", blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False, blank=True,
                                   null=True)
    updated = models.DateTimeField(auto_now=True, editable=False, blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return "Заказ #{0}".format(str(self.id))

    class Meta:
        verbose_name = "Заказ на ремонт"
        verbose_name_plural = "Заказы на ремонт"
        ordering = ["-created"]
