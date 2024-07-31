from django.shortcuts import redirect, render
from .models import Stock
import csv
from django.contrib import messages
from .forms import CSVUploadForm

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

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            
            for row in reader:
                stock, created = Stock.objects.update_or_create(
                    symbol=row['symbol'],
                    defaults={
                        'price': float(row['price']),
                        'market_cap': float(row['market_cap']),
                        'ev': float(row['ev']),
                        'ev_ebitda': float(row['ev_ebitda']),
                        'pe_ratio': float(row['pe_ratio']),
                        'pbv_ratio': float(row['pbv_ratio']),
                        'roe': float(row['roe']),
                        'roa': float(row['roa']),
                        'de_ratio': float(row['de_ratio']),
                    }
                )
            
            messages.success(request, "CSV file has been uploaded and data inserted successfully.")
            return redirect('stock_list')
    else:
        form = CSVUploadForm()

    return render(request, 'stocks/upload_csv.html', {'form': form})

