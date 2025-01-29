from django import forms
from .models import StapleItem

class StapleHandling(forms.ModelForm):
    class Meta:
        model = StapleItem
        fields = ('name', 'quantity', 'measurement_unit', 'category')
