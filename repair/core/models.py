from uuid import uuid4
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class ServiceUser(AbstractUser):
    id = models.UUIDField(
        verbose_name="Идентификатор",
        default=uuid4,
        primary_key=True
    )
    is_serviceman = models.BooleanField(
        verbose_name="Ремонтник",
        default=False,
    )
    is_team_lead = models.BooleanField(
        verbose_name="Cтарший ремонтником",
        default=False,
    )

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
    token = models.CharField(
        verbose_name="Токен",
        max_length=1500
    )


class ServiceMan(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name="User",
        on_delete=models.CASCADE,
        unique=True,
        related_name='serviceman'
    )

    def __str__(self):
        return f'Ремонтник {self.user}'

    class Meta:
        verbose_name = "Ремонтник"
        verbose_name_plural = "Ремонтники"
        ordering = ["-id"]


class Order(models.Model):
    class InnnerStatusEnum(models.TextChoices):
        CREATED = ("CREATED", "Заявка создана")
        GETTING_FROM_CLIENT = ("GETTING_FROM_CLIENT", "Получение техники от клиента")
        SENT_TO_REPAIR = ("SENT_TO_REPAIR", "Передана службе ремонта")
        REPAIR_IN_PROCESS = ("REPAIR_IN_PROCESS", "В ремонте")
        REPAIR_DONE = ("REPAIR_DONE", "Ремонт окончен")
        SENDING_TO_CLIENT = ("SENDING_TO_CLIENT", "Доставка техники клиенту")
        CLOSED = ("CLOSED", "Заявка закрыта")
    serviceman = models.ForeignKey(
        ServiceMan,
        verbose_name="Ремонтник",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    order_num = models.IntegerField(
        verbose_name='номер заказа',
        unique=True,
    )
    inner_status = models.CharField(
        verbose_name="Статус заявки",
        max_length=48,
        choices=InnnerStatusEnum.choices,
        default=InnnerStatusEnum.SENT_TO_REPAIR,
    )
    order_task = models.CharField(
        verbose_name="Неисправность со слов клиента",
        max_length=1000,
        default=""
    )
    comment = models.CharField(
        verbose_name="комментарий ремонта",
        max_length=300,
        null=True,
        blank=True,
    )
    created = models.DateTimeField(
        verbose_name="Дата и время начала ремонта", auto_now_add=True, editable=False
    )
    updated = models.DateTimeField(
        verbose_name="Дата и время изменения статуса ремонта", auto_now=True, editable=False
    )

    def __str__(self):
        return f"Ремонт id={self.id}"

    class Meta:
        verbose_name = "Ремонт"
        verbose_name_plural = "Ремонты"
        ordering = ["-created"]
