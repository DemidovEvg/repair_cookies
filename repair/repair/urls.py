"""
URL configuration for repair project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from core.views import (
    ServicemanViewSet,
    OrderViewSet,
    IndexView,
    OrderDetail,
    RepairDone,
    LoginUser,
    logout_user,
    PriceApiList,
    change_serviceman,
)

router = DefaultRouter()
router.register("servicemans", ServicemanViewSet)
router.register("orders", OrderViewSet)

urlpatterns = [
    path("", login_required(IndexView.as_view(), login_url="login"), name="home"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("<uuid:pk>/", OrderDetail.as_view(), name="order_detail"),
    path("repair_done/", RepairDone.as_view(), name="repair_done"),
    path("servisman_change/", change_serviceman, name="change_serviceman"),
    path("admin/", admin.site.urls),
    path("api/prices/", PriceApiList.as_view()),
    path("api/", include(router.urls), name="api"),
]
