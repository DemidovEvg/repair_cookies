# Generated by Django 4.2.2 on 2023-06-28 08:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_order_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="customer_description",
            field=models.CharField(default="", max_length=1000, verbose_name="Неисправность со слов клиента"),
        ),
        migrations.AddField(
            model_name="order",
            name="deliveryman_description",
            field=models.CharField(default="", max_length=1000, verbose_name="Комментарий доставки"),
        ),
        migrations.AddField(
            model_name="order",
            name="serviceman_description",
            field=models.CharField(default="", max_length=1000, verbose_name="Комментарий ремонтника"),
        ),
    ]
