# Generated by Django 4.2.2 on 2023-07-03 09:17

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(default="", max_length=250, verbose_name="Категория Техники")),
            ],
            options={
                "verbose_name": "Гаджет",
                "verbose_name_plural": "Гаджеты",
            },
        ),
        migrations.AlterModelOptions(
            name="order",
            options={
                "ordering": ["-created"],
                "verbose_name": "Заказ на ремонт",
                "verbose_name_plural": "Заказы на ремонт",
            },
        ),
        migrations.AddField(
            model_name="client",
            name="address",
            field=models.TextField(default="", verbose_name="Адрес клиента"),
        ),
        migrations.AddField(
            model_name="client",
            name="location",
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name="order",
            name="comments",
            field=models.TextField(blank=True, verbose_name="Комментарий к заказу"),
        ),
        migrations.AddField(
            model_name="order",
            name="name",
            field=models.SlugField(
                choices=[("telephone", "телефон"), ("laptop", "ноутбук"), ("tablet", "планшет")],
                max_length=200,
                null=True,
                verbose_name="Техника",
            ),
        ),
        migrations.AlterField(
            model_name="client",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=12, region="RU", unique=True, verbose_name="Номер телефона клиента"
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("CREATED", "Заказ создан"),
                    ("APPOINTED", "Заказ принят"),
                    ("IN_WORK", "Заказ в работе"),
                    ("DONE", "Заказ выполнен"),
                ],
                default="CREATED",
                max_length=12,
                verbose_name="Статус заказа",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
