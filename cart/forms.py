from django import forms

CHOICES = [(i, str(i)) for i in range(1, 16)]
# CHOICES = list(map(lambda x: (x, str(x)), range(1, 16)))


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    # quantity.widget.attrs.update({'class': 'form-control'})
