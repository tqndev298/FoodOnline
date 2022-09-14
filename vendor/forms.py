from django import forms
from .models import Vendor

class VenderForm(forms.ModelForm):
    class Meta:
        model =  Vendor
        fields = ['vendor_name','vendor_license']