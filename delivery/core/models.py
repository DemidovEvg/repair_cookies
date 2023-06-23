from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class DeliveryUser(AbstractUser):
    id = models.UUIDField(verbose_name="Идентификатор", default=uuid4, primary_key=True)

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username


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
        return f"Курьер {self.user} is_team_lead={self.is_team_lead}"

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
    class InnnerStatusEnum(models.TextChoices):
        CREATED = ("CREATED", "Заявка создана")
        APPOINTED = ("APPOINTED", "Заявка назначена")
        GETTING_FROM_CLIENT = ("GETTING_FROM_CLIENT", "Получение техники от клиента")
        SENDING_TO_REPAIR = ("SENDING_TO_REPAIR", "Доставка в службу ремонта")
        SENT_TO_REPAIR = ("SENT_TO_REPAIR", "Передана службе ремонта")
        GETTING_FROM_REPAIR = ("GETTING_FROM_REPAIR", "Получение техники от службы ремонта")
        SENDING_TO_CLIENT = ("SENDING_TO_CLIENT", "Доставка клиенту")
        SENT_TO_CLIENT = ("SENT_TO_CLIENT", "Передана клиенту")
        CLOSED = ("CLOSED", "Заявка закрыта")

    id = models.UUIDField(verbose_name="Идентификатор заказа", primary_key=True)
    phone_number = models.CharField(
        verbose_name="Номер телефона клиента", max_length=15
    )
    inner_status = models.CharField(
        verbose_name="Статус заявки",
        max_length=48,
        choices=InnnerStatusEnum.choices,
        default=InnnerStatusEnum.CREATED,
    )
    address = models.ForeignKey(
        Address,
        verbose_name="Адресс клиента",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    deliveryman = models.ForeignKey(
        Deliveryman,
        verbose_name="Курьер",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    created = models.DateTimeField(
        verbose_name="Дата и время создания заявки", auto_now_add=True, editable=False
    )
    updated = models.DateTimeField(
        verbose_name="Дата и время редактирования заявки", auto_now=True, editable=False
    )

    def __str__(self):
        return f"Заявка id={self.id}"

    class Meta:
        verbose_name = "Заявка на доставку"
        verbose_name_plural = "Заявки на доставку"
        ordering = ["-created"]

    def save(self, *args, **kwargs):
        self.change_status_event_handler(self.inner_status)
        return super().save(*args, **kwargs)

    def change_status_event_handler(self, new_inner_status):
        from core.services.order_service import UpdateOrderStatus

        if not self.id or new_inner_status == Order.InnnerStatusEnum.CREATED:
            return
        # TODO: Здесь вставить меппинг внутренних статусов на внешнии
        # Пока что просто передаем внутрении статусы
        UpdateOrderStatus.set_new_status(self.id, new_inner_status)
