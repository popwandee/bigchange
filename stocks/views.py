from django.shortcuts import render
from .models import Stock
def stock_list(request):
    stocks = Stock.objects.filter(ev_ebitda__lt=10)
    return render(request, 'stocks/stock_list.html', {'stocks': stocks})