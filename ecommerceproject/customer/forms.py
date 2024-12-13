from django import forms
from customer.models import Customermodel


class Customerform(forms.ModelForm):
    class Meta:
        models=Customermodel
        fields='__all__'