import django_filters
from django import forms
from datetime import datetime, timedelta
from core.models import Order

day = datetime.now() - timedelta(days=1)
week = datetime.now() - timedelta(weeks=1)
month = datetime.now() - timedelta(weeks=4)
DATE_CHOICES = (
    (day, "День"),
    (week, "Неделю"),
    (month, "Месяц"),
)

STATUS_CHOICES = (
    ("SENT_TO_REPAIR", "Доставлен в службу ремонта"),
    ("REPAIR_IN_PROCESS", "Ремонт начат"),
    ("REPAIR_DONE", "Ремонт закончен"),
)


class OrderFilter(django_filters.FilterSet):
    created = django_filters.ChoiceFilter(
        choices=DATE_CHOICES, lookup_expr="gte", label="Показать заказы за "
    )
    status = django_filters.ChoiceFilter(choices=STATUS_CHOICES, lookup_expr="iexact")

    class Meta:
        model = Order
        fields = ["serviceman"]
