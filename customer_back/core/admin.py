from django.contrib import admin
from core.models import Client, Order


admin.site.site_header = "Клиентская служба"


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
