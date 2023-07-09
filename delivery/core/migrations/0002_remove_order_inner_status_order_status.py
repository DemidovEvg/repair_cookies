# Generated by Django 4.2.2 on 2023-06-27 07:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="inner_status",
        ),
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("CREATED", "Заявка создана"),
                    ("GETTING_FROM_CLIENT", "Получение техники от клиента"),
                    ("SENDING_TO_REPAIR", "Доставка в службу ремонта"),
                    ("REPAIR_IN_PROCESS", "Ремонт начат"),
                    ("REPAIR_DONE", "Ремонт закончен"),
                    ("SENDING_TO_CLIENT", "Доставка техники клиенту"),
                    ("CLOSED", "Заявка закрыта"),
                ],
                default="CREATED",
                max_length=48,
                verbose_name="Статус заявки",
            ),
        ),
    ]
