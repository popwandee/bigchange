# stocks/admin_site.py

from django.contrib.admin import AdminSite
from django.urls import path
from .admin_views import upload_csv

class MyAdminSite(AdminSite):
    site_header = "Stock Admin"
    site_title = "Stock Admin Portal"
    index_title = "Welcome to Stock Admin"

    def get_urls(self):
        print("Custom admin site get_urls called")
        urls = super().get_urls()
        custom_urls = [
            path('upload-csv/', self.admin_view(upload_csv), name='upload_csv'),
        ]
        return custom_urls + urls

admin_site = MyAdminSite(name='myadmin')
