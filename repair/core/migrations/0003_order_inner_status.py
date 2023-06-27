# Generated by Django 4.2.2 on 2023-06-26 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_serviceman_is_team_lead'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='inner_status',
            field=models.CharField(choices=[('SENT_TO_REPAIR', 'Передана службе ремонта'), ('REPAIR_IN_PROGRESS', 'В ремонте'), ('GETTING_FROM_REPAIR', 'Получение техники от службы ремонта'), ('CLOSED', 'Заявка закрыта')], default='SENT_TO_REPAIR', max_length=48, verbose_name='Статус заявки'),
        ),
    ]