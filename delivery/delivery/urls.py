from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import OrderViewSet

router = DefaultRouter()
router.register("orders", OrderViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls), name="api"),
]
