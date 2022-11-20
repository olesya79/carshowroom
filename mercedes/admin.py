from django.contrib import admin

from mercedes.models import Car
from mercedes.models import Provider


# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['model', 'provider', 'price']
    search_fields = ['model__isstartwith']


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['сompany_name', 'email']
    list_filter = ['сompany_name']
