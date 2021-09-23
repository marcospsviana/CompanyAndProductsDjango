from django import forms
from .models import Product


class CreateProduct(forms.ModelForm):

    company = forms.ChoiceField()
    product = forms.CharField()

    class Meta:
        fields = ["company", "product"]
        model = Product
