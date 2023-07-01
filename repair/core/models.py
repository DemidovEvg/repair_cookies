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
    class StatusEnum(models.TextChoices):
        CREATED = ("CREATED", "Заявка создана")
        GETTING_FROM_CLIENT = ("GETTING_FROM_CLIENT", "Получение техники от клиента")
        SENT_TO_REPAIR = ("SENT_TO_REPAIR", "Доставлен в службу ремонта")
        REPAIR_IN_PROCESS = ("REPAIR_IN_PROCESS", "Ремонт начат")
        REPAIR_DONE = ("REPAIR_DONE", "Ремонт закончен")
        SENDING_TO_CLIENT = ("SENDING_TO_CLIENT", "Доставка техники клиенту")
        CLOSED = ("CLOSED", "Заявка закрыта")
    serviceman = models.ForeignKey(
        ServiceMan,
        verbose_name="Ремонтник",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    id = models.UUIDField(
        verbose_name="Идентификатор заказа",
        primary_key=True
    )
    status = models.CharField(
        verbose_name="Статус заявки",
        max_length=48,
        choices=StatusEnum.choices,
        default=StatusEnum.CREATED,
    )
    serviceman_description = models.CharField(
        verbose_name="Комментарий ремонтника",
        max_length=1000,
        default=""
    )
    customer_description = models.CharField(
        verbose_name="Неисправность со слов клиента",
        max_length=1000,
        default=""
    )
    deliveryman_description = models.CharField(
        verbose_name="Комментарий доставки",
        max_length=1000,
        default=""
    )
    comment = models.TextField(
        verbose_name="Комментарии",
        default='')
    created = models.DateTimeField(
        verbose_name="Дата и время создания заявки",
        editable=False
    )
    updated = models.DateTimeField(
        verbose_name="Дата и время редактирования заявки",
        auto_now=True,
        editable=False
    )
    amount_due_by = models.FloatField(
        verbose_name="Сумма к оплате",
        default=0)
    payment_completed = models.BooleanField(
        verbose_name="Оплала произведена?",
        default=False
    )
    address = models.UUIDField(
        verbose_name="Адресс клиента",
        null=True,
        blank=True,
    )
    client = models.UUIDField(
        verbose_name="Клиент",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Ремонт id={self.id}"

    class Meta:
        verbose_name = "Ремонт"
        verbose_name_plural = "Ремонты"
        ordering = ["-created"]
