from django.db import models
from django.contrib.auth.models import User


class ServiceUser(User):
    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username


class ServiceMan(models.Model):
    user = models.OneToOneField(
        ServiceUser,
        verbose_name="Ремонтник",
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
