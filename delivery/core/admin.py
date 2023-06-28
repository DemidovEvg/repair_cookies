from django.contrib import admin
from django.contrib import messages
from django.conf import settings

from core.models import Deliveryman, Order, Address, City, DeliveryUser
from core.services.order_service import create_or_update
from core.serializers import OrderSerializer


admin.site.site_header = "Доставщики"


@admin.register(DeliveryUser)
class DeliveryUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Deliveryman)
class DeliverymanAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "phone_number", "status", "deliveryman", "created"]
    fields = [
        "id",
        "phone_number",
        "status",
        "address",
        "deliveryman",
        "serviceman_description",
        "customer_description",
        "deliveryman_description",
        "comment",
        "created",
        "updated",
    ]
    readonly_fields = ["created", "updated", "serviceman_description"]
    list_filter = ["deliveryman"]
    list_editable = ["status"]

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
            raise ExceptionGroup("Ошибки обновления", exceptions)
        
@admin.register(Address)
class AdressAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass
