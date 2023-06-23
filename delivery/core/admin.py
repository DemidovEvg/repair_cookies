from django.contrib import admin
from django.http import HttpResponseRedirect
from core.models import Deliveryman, Order, Address, City, DeliveryUser


admin.site.site_header = "Доставщики"

@admin.register(DeliveryUser)
class DeliveryUserAdmin(admin.ModelAdmin):
    pass

@admin.register(Deliveryman)
class DeliverymanAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "phone_number", "inner_status", "deliveryman", "created"]
    fields = [
        "id",
        "phone_number",
        "inner_status",
        "address",
        "deliveryman",
        "created",
        "updated",
    ]
    readonly_fields = ["created", "updated"]
    list_filter = ["deliveryman"]
    list_editable = ["inner_status"]

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
