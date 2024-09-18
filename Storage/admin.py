from django.contrib import admin
from Storage.models import BrandsFood, PetFoods

# Register your models here.

@admin.register(BrandsFood)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ("id", "brand")
    search_fields = ('brand',)


@admin.register(PetFoods)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "weight", "quantity", "quantity_alert", "buy_price", "sell_price")
    search_fields = ('name', 'weight')