from django.urls import path

from . import views

app_name = 'vendingmachine'
urlpatterns = [
    path('', views.index, name='index'),
    path('purchase/<item_id>/', views.purchase, name='purchase'),
    path('add/', views.top_up, name='add'),
    path('flush', views.flush, name='flush'),
]
