from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stock_list/', views.stock_list, name='stock_list'),
    path('load_data/', views.load_data, name='load_data'),
    path('apply_filter/', views.apply_filter, name='apply_filter'),
]