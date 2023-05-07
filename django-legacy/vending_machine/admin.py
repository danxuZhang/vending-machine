from django.contrib import admin

from .models import Beverage, Transaction
# Register your models here.
admin.site.register(Beverage)
admin.site.register(Transaction)
