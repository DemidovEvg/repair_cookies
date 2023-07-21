from django.contrib import admin
from .models import Order, ServiceMan, ServiceUser, Price

admin.site.register(Order)
admin.site.register(ServiceMan)
admin.site.register(ServiceUser)
admin.site.register(Price)
