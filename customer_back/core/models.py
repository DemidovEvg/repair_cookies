from customer.settings import PHONE_NUMBER_REGION
from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Client(AbstractUser):
    phone_number = PhoneNumberField(
        unique=True, region=PHONE_NUMBER_REGION, max_length=12
    )


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    deleted = models.BooleanField(default=False)
