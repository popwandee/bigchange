# myapp/forms.py

from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['name', 'ev_ebitda', 'details']  # Include all fields you want to use in the form
