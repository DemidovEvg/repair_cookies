from django.db import models
from django.contrib.auth.models import User


class ProxyUser(User):
    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username

    class Meta:
        proxy = True


class Deliveryman(models.Model):
    user = models.OneToOneField(
        ProxyUser,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        unique=True,
        related_name='deliveryman'
    )
    is_team_lead = models.BooleanField(
        verbose_name="Является старшим доставщиком", default=False
    )

    def __str__(self):
        return f'Курьер {self.user} is_team_lead={self.is_team_lead}'

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
        return f"{self.city} {self.street} {self.home}"

    class Meta:
        verbose_name = "Адресс"
        verbose_name_plural = "Адрессы"
        ordering = ["-id"]


class Order(models.Model):
    class StatusEnum(models.TextChoices):
        CREATED = ("CREATED", "Заявка создана")
        APPOINTED = ("APPOINTED", "Заявка назначена")
        IN_WORK = ("IN_WORK", "Заявка в работе")
        DONE = ("DONE", "Заявка выполнена")

    id = models.UUIDField(verbose_name="Идентификатор заказа", primary_key=True)
    phone_number = models.CharField(
        verbose_name="Номер телефона клиента", max_length=15
    )
    status = models.CharField(
        verbose_name="Статус заявки",
        max_length=12,
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
