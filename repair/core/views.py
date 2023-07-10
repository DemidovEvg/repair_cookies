from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from rest_framework.viewsets import ModelViewSet
from django.views.generic import UpdateView, ListView

from .models import ServiceMan, Order
from .serializers import ServicemanModelSerializer, OrderModelSerializer
from permissions import ServicemanPermissions, OrderPermissions
from .services.order_service import update_outer_order
from .serializers import OrderModelSerializer
from .forms import OrderUpdateForm
from .services.filter_service import time_filter


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer
    permission_classes = (OrderPermissions,)


class ServicemanViewSet(ModelViewSet):
    queryset = ServiceMan.objects.all()
    serializer_class = ServicemanModelSerializer
    permission_classes = (ServicemanPermissions,)


class IndexView(ListView):
    model = Order
    template_name = "index.html"
    context_object_name = "orders"
    fields = ["serviceman"]

    def get_queryset(self):
        fltr = time_filter(self.request.GET)
        if self.request.user.is_team_lead and fltr:
            return Order.objects.filter(created__gte=fltr)
        elif self.request.user.is_team_lead:
            return Order.objects.all()

        if fltr:
            return Order.objects.filter(
                serviceman=self.request.user.serviceman.id, created__gte=fltr
            )

        return Order.objects.filter(serviceman=self.request.user.serviceman.id)


class OrderDetail(UpdateView):
    model = Order

    template_name = "order_detail.html"
    context_object_name = "order"
    fields = ["serviceman", "serviceman_description", "status", "amount_due_by"]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        self.object = self.get_object()
        payload = OrderModelSerializer(instance=self.object).data
        pk = self.object.id

        try:
            service_update = f"{settings.CLIENT_SERVICE}/api/orders/{pk}/"
            update_outer_order(service_update, payload)
        except Exception as exc:
            messages.add_message(request, messages.ERROR, repr(exc))

        try:
            service_update = f"{settings.DELIVERY_SERVICE}/api/orders/{pk}/"
            update_outer_order(service_update, payload)
        except Exception as exc:
            messages.add_message(request, messages.ERROR, repr(exc))

        return HttpResponseRedirect(reverse_lazy("order_detail", kwargs={"pk": pk}))

    def get_success_url(self):
        pass


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "login.html"

    def get_success_url(self):
        return reverse_lazy("home")


def logout_user(request):
    logout(request)

    return redirect("login")


def change_rm(request, **kwargs):
    pass
