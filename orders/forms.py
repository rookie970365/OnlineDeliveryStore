from django import forms
from .models import Order
from django.forms import Widget


class FormStylesMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # print(name, field, field.widget)
            widget: Widget = field.widget
            widget.attrs["class"] = "form-control"


class OrderCreateForm(FormStylesMixin, forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postcode', 'city']
