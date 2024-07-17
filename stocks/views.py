from django.shortcuts import redirect, render
from .models import Stock

def stock_list(request):
    stocks = Stock.objects.filter(ev_ebitda__lt=10)
    return render(request, 'stocks/stock_list.html', {'stocks': stocks})

def index(request):
    stocks = Stock.objects.all()
    return render(request, 'stocks/index.html', {'stocks': stocks})

def load_data(request):
    # Logic to load data
    return redirect('index')

def apply_filter(request):
    # Logic to apply filter
    return redirect('index')