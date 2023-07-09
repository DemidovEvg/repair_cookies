from django.contrib import admin
from django.contrib import messages
from django.conf import settings

from core.models import Client, Order
from core.serializers import OrderModelSerializer
from core.serializers import ClientModelSerializer

from core.services.order_service import create_or_update

admin.site.site_header = "Клиентская служба"


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("first_name", "phone_number")

    def save_model(self, request, obj, form, change):
        obj.save()
        try:
            self.create_or_update_outer_order(obj)
        except Exception as exc:
            messages.add_message(request, messages.ERROR, repr(exc))

    def create_or_update_outer_order(self, order: Order):
        exceptions = []
        try:
            service_create = f"{settings.CLIENT_SERVICE}/api/users/"
            service_update = f"{service_create}{order.id}/"
            data = ClientModelSerializer(instance=order).data

            create_or_update(service_create, service_update, data)
        except Exception as exc:
            exceptions.append(exc)

        try:
            service_create = f"{settings.REPAIR_SERVICE}/api/users/"
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

    class Meta:
        ordering = ("username", "phone_number")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.save()
        try:
            self.create_or_update_outer_order(obj)
        except Exception as exc:
            messages.add_message(request, messages.ERROR, repr(exc))

    def create_or_update_outer_order(self, order: Order):
        exceptions = []
        try:
            service_create = f"{settings.DELIVERY_SERVICE}/api/orders/"
            service_update = f"{service_create}{order.id}/"
            data = OrderModelSerializer(instance=order).data

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
