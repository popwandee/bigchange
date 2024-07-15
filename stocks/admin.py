from django.contrib import admin
from django.urls import path
from .models import Stock, StockCSV
from .admin_views import upload_csv
from .admin_site import admin_site

#@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('name','ev','ebitda', 'ev_ebitda','roe','roa','pe','pbv')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('upload-csv/', self.admin_site.admin_view(upload_csv), name='upload_csv'),
        ]
        return custom_urls + urls

admin.site.register(Stock,StockAdmin)

@admin.register(StockCSV, site=admin_site)
class StockCSVAdmin(admin.ModelAdmin):
    pass

