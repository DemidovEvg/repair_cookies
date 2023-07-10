from django import forms
from .models import *


class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["serviceman_description", "status", "amount_due_by"]
        widgets = {
            "serviceman_description": forms.Textarea(attrs={"cols": 60, "rows": 10})
        }
