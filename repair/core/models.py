from customer.settings import PHONE_NUMBER_REGION
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from uuid import uuid4

from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Client(AbstractUser):
    id = models.UUIDField(verbose_name="Идентификатор", default=uuid4, primary_key=True)
    phone_number = PhoneNumberField(
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


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    deleted = models.BooleanField(default=False)
