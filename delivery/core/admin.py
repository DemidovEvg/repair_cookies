from django.contrib import admin
from django.contrib import messages
from django.conf import settings
from django import forms
from django.db import models

from core.models import Deliveryman, Order, Address, City, DeliveryUser, Client
from core.services.order_service import create_or_update
from core.serializers import OrderSerializer


admin.site.site_header = "Доставщики"


@admin.register(DeliveryUser)
class DeliveryUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Deliveryman)
class DeliverymanAdmin(admin.ModelAdmin):
    pass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


class DeliveryStatusEnum(models.TextChoices):
    EMPTY = ("", "---------")
    GETTING_FROM_CLIENT = ("GETTING_FROM_CLIENT", "Получение техники от клиента")
    SENT_TO_REPAIR = ("SENT_TO_REPAIR", "Доставлен в службу ремонта")
    SENDING_TO_CLIENT = ("SENDING_TO_CLIENT", "Доставка техники клиенту")
    CLOSED = ("CLOSED", "Заявка закрыта")


class OrderAdminForm(forms.ModelForm):
    new_status = forms.fields.ChoiceField(
        choices=DeliveryStatusEnum.choices, label="Новый статус", required=False
    )

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data.get("new_status"):
            instance.status = self.cleaned_data.get("new_status")
        if commit:
            instance.save()
        return instance


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm
    list_display = [
        "id",
        "status_common",
        "deliveryman",
        "created",
        "address",
        "deliveryman_description",
    ]
    fields = [
        "short_id",
        "client",
        "status_common",
        "new_status",
        "category",
        "address",
        "deliveryman",
        "serviceman_description",
        "customer_description",
        "deliveryman_description",
        "created",
        "updated",
        "payment_completed",
        "amount_due_by",
    ]
    readonly_fields = [
        "short_id",
        "status_common",
        "deliveryman",
        "created",
        "updated",
        "serviceman_description",
        "amount_due_by",
    ]
    list_filter = ["deliveryman", "created"]
    list_editable = ["deliveryman"]

    def get_changelist_instance(self, request):
        changelist_instance = super().get_changelist_instance(request)
        if not request.user.is_superuser and not request.user.deliveryman.is_team_lead:
            list_editable = list(changelist_instance.list_editable)
            list_editable.remove("deliveryman")
            changelist_instance.list_editable = list_editable
        return changelist_instance

    @admin.display(description="Короткий id")
    def short_id(self, obj):
        return obj.id.int % (10 * 4)

    @admin.display(description="Текущий статус")
    def status_common(self, obj):
        return obj.get_status_display()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        user = request.user
        if user.is_superuser:
            return qs
        if not user.deliveryman:
            return []
        deliveryman = user.deliveryman
        if deliveryman.is_team_lead:
            return qs
        return qs.filter(deliveryman=deliveryman)

    def save_model(self, request, obj, form, change):
        obj.save()
        try:
            self.create_or_update_outer_order(obj)
        except Exception as exc:
            messages.add_message(request, messages.ERROR, repr(exc))

    def create_or_update_outer_order(self, order: Order):
        exceptions = []
        try:
            service_create = f"{settings.CLIENT_SERVICE}/api/orders/"
            service_update = f"{service_create}{order.id}/"
            data = OrderSerializer(instance=order).data

            create_or_update(service_create, service_update, data)
        except Exception as exc:
            exceptions.append(exc)

        try:
            service_create = f"{settings.REPAIR_SERVICE}/api/orders/"
            service_update = f"{service_create}{order.id}/"
            create_or_update(service_create, service_update, data)
        except Exception as exc:
            exceptions.append(exc)

        if exceptions:
            raise Exception(repr(exceptions))

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(Address)
class AdressAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass
