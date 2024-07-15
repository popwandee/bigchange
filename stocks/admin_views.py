# stocks/admin_views.py
import csv
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import StockCSVForm
from io import TextIOWrapper
from .models import Stock

def upload_csv(request):
        if request.method == 'POST':
            form = StockCSVForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                csv_file = request.FILES['file']

                if not csv_file.name.endswith('.csv'):
                    messages.error(request, 'This is not a CSV file')
                    return redirect('admin:upload_csv')

                file_data = csv_file.read().decode('utf-8')
                lines = file_data.split('\n')
                for line in lines:
                    fields = line.split(',')
                    if len(fields) >= 2:  # Adjust based on your CSV structure
                        stock_name = fields[0].strip()
                        ev_ebitda = fields[1].strip()
                        stock, created = Stock.objects.update_or_create(
                            name=stock_name,
                            defaults={'ev_ebitda': ev_ebitda}
                        )
                messages.success(request, 'CSV file has been processed successfully')
                return redirect('admin:upload_csv')
        else:
            form = StockCSVForm()
        return render(request, 'admin/upload_csv.html', {'form': form})

