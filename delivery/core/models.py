from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils import timezone


class DeliveryUser(AbstractUser):
    id = models.UUIDField(verbose_name="Идентификатор", default=uuid4, primary_key=True)
    middle_name = models.CharField("Отчетство", max_length=150, blank=True)

    def __str__(self):
        middle_name_first_letter = (
            self.middle_name[0:1] if len(self.middle_name) else ""
        )
        first_name_first_letter = self.first_name[0:1] if len(self.first_name) else ""
        full_name = ""
        if self.first_name and self.last_name:
            full_name += self.last_name
            full_name += f" {first_name_first_letter}."
            if middle_name_first_letter:
                full_name += f"{middle_name_first_letter}."
        full_name += f" ({self.username})"
        return full_name


class TokenData(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        unique=True,
        related_name="token_data",
    )
    token = models.CharField(verbose_name="Токен", max_length=1500)


class Deliveryman(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        unique=True,
        related_name="deliveryman",
    )
    is_team_lead = models.BooleanField(
        verbose_name="Является старшим доставщиком", default=False
    )

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = "Курьер"
        verbose_name_plural = "Курьеры"
        ordering = ["-id"]


class City(models.Model):
    name = models.CharField(verbose_name="Название города", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        ordering = ["-id"]


class Address(models.Model):
    city = models.ForeignKey(City, verbose_name="Город", on_delete=models.CASCADE)
    street = models.CharField(verbose_name="Улица", max_length=255)
    building = models.CharField(verbose_name="Номер дома", max_length=16)
    apartment = models.IntegerField(verbose_name="Номер квартиры")

    def __str__(self):
        return f"{self.city} {self.street} {self.building} {self.apartment}"

    class Meta:
        verbose_name = "Адресс"
        verbose_name_plural = "Адрессы"
        ordering = ["-id"]


class Order(models.Model):
    class StatusEnum(models.TextChoices):
        CREATED = ("CREATED", "Заявка создана")
        GETTING_FROM_CLIENT = ("GETTING_FROM_CLIENT", "Получение техники от клиента")
        SENT_TO_REPAIR = ("SENT_TO_REPAIR", "Доставлен в службу ремонта")
        REPAIR_IN_PROCESS = ("REPAIR_IN_PROCESS", "Ремонт начат")
        REPAIR_DONE = ("REPAIR_DONE", "Ремонт закончен")
        SENDING_TO_CLIENT = ("SENDING_TO_CLIENT", "Доставка техники клиенту")
        CLOSED = ("CLOSED", "Заявка закрыта")

    id = models.UUIDField(verbose_name="Идентификатор заказа", primary_key=True)
    phone_number = models.CharField(
        verbose_name="Номер телефона клиента", max_length=15
    )
    status = models.CharField(
        verbose_name="Статус заявки",
        max_length=48,
        choices=StatusEnum.choices,
        default=StatusEnum.CREATED,
    )
    address = models.ForeignKey(
        Address,
        verbose_name="Адресс клиента",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
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
    deliveryman = models.ForeignKey(
        Deliveryman,
        verbose_name="Курьер",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    comment = models.TextField(verbose_name="Комментарии", default="", blank=True)
    created = models.DateTimeField(
        verbose_name="Дата и время создания заявки", default=timezone.now
    )
    updated = models.DateTimeField(
        verbose_name="Дата и время редактирования заявки", auto_now=True
    )
    payment_completed = models.BooleanField(
        verbose_name="Оплала произведена?", default=False
    )
    amount_due_by = models.FloatField(verbose_name="Сумма к оплате", default=0)

    def __str__(self):
        return f"Заявка id={self.id}"

    class Meta:
        verbose_name = "Заявка на доставку"
        verbose_name_plural = "Заявки на доставку"
        ordering = ["-created"]
