from django.contrib import admin
from django.urls import path
from .models import Stock

#@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('name','ev','ebitda', 'ev_ebitda','roe','roa','pe','pbv')

admin.site.register(Stock,StockAdmin)