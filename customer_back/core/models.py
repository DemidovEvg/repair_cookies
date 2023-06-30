from customer.settings import PHONE_NUMBER_REGION
from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Client(AbstractUser):
    address = models.TextField("Адрес клиента", default='')
    location = models.CharField(max_length=30, blank=True)
    phone_number = PhoneNumberField("Номер телефона клиента",
        unique=True, region=PHONE_NUMBER_REGION, max_length=12
    )


class Category(models.Model):
    '''Вид техники'''
    name = models.CharField(max_length=250, default='')


class Order(models.Model):
    class StatusEnum(models.TextChoices):
        CREATED = ("CREATED", "Заявка создана")
        APPOINTED = ("APPOINTED", "Заявка назначена")
        IN_WORK = ("IN_WORK", "Заявка в работе")
        DONE = ("DONE", "Заявка выполнена")
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(
        verbose_name="Статус заявки",
        max_length=12,
        choices=StatusEnum.choices,
        default=StatusEnum.CREATED,
    )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return "Заказ #{0}".format(str(self.id))
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

