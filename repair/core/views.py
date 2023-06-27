from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from rest_framework.viewsets import ModelViewSet
from django.views.generic import ListView, DetailView

from core.models import ServiceMan, Order
from core.serializers import ServicemanModelSerializer, OrderModelSerializer
from permissions import ServicemanPermissions, OrderPermissions


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer
    permission_classes = (
        OrderPermissions,
    )


class ServicemanViewSet(ModelViewSet):
    queryset = ServiceMan.objects.all()
    serializer_class = ServicemanModelSerializer
    permission_classes = (
        ServicemanPermissions,
    )


class IndexView(ListView):
    model = Order
    template_name = 'index.html'
    context_object_name = "orders"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicemans'] = ServiceMan.objects.all()
        return context


class OrderDetail(DetailView):
    model = Order
    template_name = 'order_detail.html'
    context_object_name = "order"


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
