from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from django.views.generic import UpdateView, ListView

from .models import ServiceMan, Order, Price
from .serializers import (
    ServicemanModelSerializer,
    OrderModelSerializer,
    PriceModelSerializer,
)
from permissions import ServicemanPermissions, OrderPermissions
from .services.order_service import update_outer_order
from .services.get_price import get_repair_price
from .serializers import OrderModelSerializer
from .filters import OrderFilter
from .forms import ServicemanUpdateForm


class PriceApiList(ListAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceModelSerializer


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
    paginate_by = 5

    def get_queryset(self):
        queryset = Order.get_for_user(user=self.request.user)
        self.filterset = OrderFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        context["f"] = ServicemanUpdateForm
        return context


class OrderDetail(UpdateView):
    model = Order

    template_name = "order_detail.html"
    context_object_name = "order"
    fields = ["serviceman_description", "status", "repair_lvl"]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        self.object = self.get_object()
        payload = OrderModelSerializer(instance=self.object).data

        if payload["repair_lvl"] != Order.RepairLvl.UNDEFINED.value:
            price = get_repair_price(payload["category"], payload["repair_lvl"])
            payload["amount_due_by"] = price.price
            self.object.amount_due_by = price.price
            self.object.save(update_fields=["amount_due_by"])

        pk = self.object.id

        try:
            service_update = f"{settings.CLIENT_SERVICE}/api/orders/{pk}/sync/"
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


class RepairDone(ListView):
    model = Order
    template_name = "repair_done.html"
    context_object_name = "orders"
    paginate_by = 5

    def get_queryset(self):
        valid_status = ["REPAIR_DONE", "SENDING_TO_CLIENT", "CLOSED"]
        queryset = Order.objects.filter(status__in=valid_status)

        return queryset


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "login.html"

    def get_success_url(self):
        return reverse_lazy("home")


def logout_user(request):
    logout(request)

    return redirect("login")


def change_serviceman(request):
    serviceman = ServiceMan.objects.get(user=request.GET.get("user"))
    obj = Order.objects.get(id=request.GET.get("order_id"))
    obj.serviceman = serviceman
    obj.save()

    return redirect("home")
