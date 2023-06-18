from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from uuid import uuid4

# Create your models here.
phone_regex = RegexValidator(
    regex=r"^\d{4,15}$",
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
)


class Client(AbstractUser):
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=15,
        unique=True,
    )


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    deleted = models.BooleanField(default=False)
