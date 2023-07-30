from django import forms
from .models import *


class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["serviceman_description", "status", "amount_due_by"]
        widgets = {
            "serviceman_description": forms.Textarea(attrs={"cols": 60, "rows": 10})
        }


class ServicemanUpdateForm(forms.ModelForm):
    class Meta:
        model = ServiceMan
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user"].empty_label = "Ремонтник не выбран"
