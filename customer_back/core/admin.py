from django.contrib import admin
from django.contrib import messages
from django.conf import settings
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from core.models import Client, Order, RepairKind, Price
from core.serializers import OrderModelSerializer

from core.services.order_service import create_or_update

admin.site.site_header = "Клиентская служба"


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    def save_model(self, request, obj: Order, form, change):
        obj.save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"sync_client_orders_channel_group_{obj.client_id}",
            {"type": "websocket.receive", "text": f"update_order order_id={obj.id}"},
        )
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


@admin.register(RepairKind)
class RepairKindAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "equipment_category",
        "repair_kind_name",
        "repair_subkind_name",
        "name",
        "value",
    ]

    @admin.display(description="Вид ремонта")
    def repair_kind_name(self, obj: Price):
        return obj.repair_kind.name

    @admin.display(description="Подвид ремонта")
    def repair_subkind_name(self, obj: Price):
        return obj.repair_subkind and obj.repair_subkind.name
