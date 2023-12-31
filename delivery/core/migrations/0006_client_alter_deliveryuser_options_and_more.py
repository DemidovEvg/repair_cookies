# Generated by Django 4.2.2 on 2023-06-29 13:24

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_deliveryuser_middle_name_order_amount_due_by_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Идентификатор",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(blank=True, max_length=150, verbose_name="Имя"),
                ),
                (
                    "middle_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="Отчетство"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="Фамилия"
                    ),
                ),
                (
                    "email",
                    models.EmailField(blank=True, max_length=254, verbose_name="Почта"),
                ),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=12, region="RU", unique=True
                    ),
                ),
            ],
            options={
                "verbose_name": "Клиент",
                "verbose_name_plural": "Клиенты",
                "ordering": ["-id"],
            },
        ),
        migrations.AlterModelOptions(
            name="deliveryuser",
            options={
                "ordering": ["-id"],
                "verbose_name": "Доставщик",
                "verbose_name_plural": "Доставщики",
            },
        ),
        migrations.RemoveField(
            model_name="order",
            name="phone_number",
        ),
        migrations.AlterField(
            model_name="order",
            name="comment",
            field=models.TextField(blank=True, default="", verbose_name="Комментарии"),
        ),
        migrations.AlterField(
            model_name="order",
            name="customer_description",
            field=models.CharField(
                blank=True,
                default="",
                max_length=1000,
                verbose_name="Неисправность со слов клиента",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="deliveryman_description",
            field=models.CharField(
                blank=True,
                default="",
                max_length=1000,
                verbose_name="Комментарий доставки",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="serviceman_description",
            field=models.CharField(
                blank=True,
                default="",
                max_length=1000,
                verbose_name="Комментарий ремонтника",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="client",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.client",
                verbose_name="Клиент",
            ),
            preserve_default=False,
        ),
    ]
