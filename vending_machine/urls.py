from django.urls import path

from . import views

app_name = 'vendingmachine'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.top_up, name='add'),
    path('flush', views.flush, name='flush'),
    path('purchase/', views.purchase, name='purchase'),
    path('history/', views.history, name='history'),
]
