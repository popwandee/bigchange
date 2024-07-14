from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Stock
from .forms import StockForm
# Create your views here.

def stock_list(request):
    stocks = Stock.objects.all()
    return render(request, 'myapp/stock_list.html', {'stocks': stocks})

def stock_list_ev_ebitda(request):
    stocks = Stock.objects.all()
    filtered_stocks = [stock for stock in stocks if stock.ev_ebitda_ratio() < 10]
    return render(request, 'stock_list.html', {'stocks': filtered_stocks})

def stock_detail(request, stock_id):
    stock = Stock.objects.get(id=stock_id)
    return render(request, 'stock_detail.html', {'stock': stock})

def add_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_list')
    else:
        form = StockForm()
    return render(request, 'myapp/add_stock.html', {'form': form})

def update_stock(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('stock_list')
    else:
        form = StockForm(instance=stock)
    return render(request, 'myapp/update_stock.html', {'form': form})

def delete_stock(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id)
    if request.method == 'POST':
        stock.delete()
        return redirect('stock_list')
    return render(request, 'myapp/delete_stock.html', {'stock': stock})
