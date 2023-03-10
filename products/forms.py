from django import forms
from django.forms import Widget
from products.models import ProductKind, ProductOrigin


# class FormStylesMixin:
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         for name, field in self.fields.items():
#             print(name, field, field.widget)
#             widget: Widget = field.widget
#             widget.attrs["class"] = "button"


class FilterByKindForm(forms.Form):
    choice = forms.ModelChoiceField(queryset=ProductKind.objects.all(), label="",
                                    empty_label="--------------------")
    # by_kind.widget.attrs.update({'class': 'form-control'})


class FilterByOriginForm(forms.Form):
    by_origin = forms.ModelChoiceField(queryset=ProductOrigin.objects.all(), label="",
                                    empty_label="--------------------")

