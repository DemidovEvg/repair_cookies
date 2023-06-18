from django.contrib import admin
from .models import Order, ServiceMan, SimpleUser

admin.site.register(Order)
admin.site.register(ServiceMan)
admin.site.register(SimpleUser)
