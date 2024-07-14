from django.shortcuts import render

# Create your views here.
from .models import Stock

def stock_list(request):
    stocks = Stock.objects.all()
    filtered_stocks = [stock for stock in stocks if stock.ev_ebitda_ratio() < 10]
    return render(request, 'stock_list.html', {'stocks': filtered_stocks})

def stock_detail(request, stock_id):
    stock = Stock.objects.get(id=stock_id)
    return render(request, 'stock_detail.html', {'stock': stock})