# stocks/forms.py
from django import forms
from .models import StockCSV

class StockCSVForm(forms.ModelForm):
    class Meta:
        model = StockCSV
        fields = ['file']
