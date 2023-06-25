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


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, default='Техника')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_ORDER_CHOICES = [
        ("IP", " В обработке"),
        ("AP", "Ожидает оплаты"),
        ("P", "Принят к исполнению"),
        ("S", "Отправлен"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='техника', default="техника")
    status = models.CharField(
        max_length=2,
        choices=STATUS_ORDER_CHOICES,
        default="IP",
    )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'Заказ {self.id} is_status={self.status}'

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
