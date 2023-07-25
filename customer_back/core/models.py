from uuid import uuid4

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from customer.settings import PHONE_NUMBER_REGION


# Create your models here.


class Client(AbstractUser):
    id = models.UUIDField(verbose_name="Идентификатор", default=uuid4, primary_key=True)
    email = models.EmailField("email", unique=True, validators=[EmailValidator])
    patronymic = models.CharField("Отчество", max_length=150, blank=True, default="")
    address = models.TextField("Адрес клиента", default="")
    location = models.CharField(max_length=30, blank=True)
    phone_number = PhoneNumberField(
        "Номер телефона клиента", unique=True, region=PHONE_NUMBER_REGION, max_length=12
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


class Order(models.Model):
    class StatusEnum(models.TextChoices):
        CREATED = ("CREATED", "Заявка создана")
        GETTING_FROM_CLIENT = ("GETTING_FROM_CLIENT", "Получение техники от клиента")
        SENT_TO_REPAIR = ("SENT_TO_REPAIR", "Доставлен в службу ремонта")
        REPAIR_IN_PROCESS = ("REPAIR_IN_PROCESS", "Ремонт начат")
        REPAIR_DONE = ("REPAIR_DONE", "Ремонт закончен")
        SENDING_TO_CLIENT = ("SENDING_TO_CLIENT", "Доставка техники клиенту")
        CLOSED = ("CLOSED", "Заявка закрыта")

    class GadgetType(models.TextChoices):
        TELEPHONE = ("TELEPHONE", "телефон")
        LAPTOP = ("LAPTOP", "ноутбук")
        TABLET = ("TABLET", "планшет")

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="orders")
    status = models.CharField(
        verbose_name="Статус заказа",
        max_length=48,
        choices=StatusEnum.choices,
        default=StatusEnum.CREATED,
    )
    category = models.CharField(
        "Техника",
        max_length=15,
        choices=GadgetType.choices,
    )
    model = models.CharField(
        verbose_name="Модель техники", max_length=1000, default="", blank=True
    )
    serviceman_description = models.CharField(
        verbose_name="Комментарий ремонтника", max_length=1000, default="", blank=True
    )
    customer_description = models.CharField(
        verbose_name="Неисправность со слов клиента",
        max_length=1000,
        default="",
        blank=True,
    )
    deliveryman_description = models.CharField(
        verbose_name="Комментарий доставки", max_length=1000, default="", blank=True
    )
    created = models.DateTimeField(
        auto_now_add=True, editable=False, blank=True, null=True
    )
    updated = models.DateTimeField(auto_now=True, editable=False, blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return "Заказ #{0}".format(str(self.id))

    class Meta:
        verbose_name = "Заказ на ремонт"
        verbose_name_plural = "Заказы на ремонт"
        ordering = ["-created"]


class RepairKind(models.Model):
    name = models.CharField(
        "Название",
        max_length=100,
    )

    def __str__(self):
        return f"RepairKind---id={self.id}---name={self.name}"

    class Meta:
        verbose_name = "Вид ремонта"
        verbose_name_plural = "Виды ремонта"


class Price(models.Model):
    GadgetType = Order.GadgetType

    equipment_category = models.CharField(
        "Техника",
        max_length=15,
        choices=Order.GadgetType.choices,
    )
    repair_kind = models.ForeignKey(
        to=RepairKind,
        verbose_name="Вид ремонта",
        on_delete=models.CASCADE,
        related_name="prices_for_kind",
    )
    repair_subkind = models.ForeignKey(
        to=RepairKind,
        verbose_name="Подвид ремонта",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="prices_for_subkind",
    )
    name = models.CharField(
        "Название ремонта",
        max_length=100,
    )

    value = models.DecimalField("Цена", max_digits=12, decimal_places=2, default=0.0)

    def __str__(self):
        return (
            f"Price---id={self.id}---"
            f"equipment_category={self.equipment_category}---"
            f"repair_kind={self.repair_kind_id}---value={self.value}"
        )

    class Meta:
        verbose_name = "Расценка на ремонт"
        verbose_name_plural = "Расценки на ремонт"
