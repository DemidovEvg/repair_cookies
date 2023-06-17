from django.contrib import admin
from core.models import Deliveryman, Order, Address, City, ProxyUser


admin.site.site_header = "Доставщики"


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
        "created",
        "updated",
    ]
    readonly_fields = ["id", "phone_number", "created", "updated"]
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


@admin.register(Address)
class AdressAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass
