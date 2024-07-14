"""
URL configuration for bigchange project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

# stock_app/urls.py

urlpatterns = [
    path('stock_admin/', admin.site.urls,name='stock_admin'),
    path('', views.stock_list, name='stock_list'),
    path('stock/<int:stock_id>/', views.stock_detail, name='stock_detail'),
    path('add_stock/', views.add_stock, name='add_stock'),
    path('update_stock/<int:stock_id>/', views.update_stock, name='update_stock'),
    path('delete_stock/<int:stock_id>/', views.delete_stock, name='delete_stock'),
]
