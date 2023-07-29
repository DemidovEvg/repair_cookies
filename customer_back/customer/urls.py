from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from core.views import ClientViewSet, OrderViewSet, PriceViewSet, client_orders

router = DefaultRouter()
router.register("users", ClientViewSet)
router.register("orders", OrderViewSet)
router.register("prices", PriceViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls), name="api"),
    path("api-token-auth/", views.obtain_auth_token, name="token_auth"),
    path("ws/client-orders/<str:email>/", client_orders, name="client_orders"),
]
