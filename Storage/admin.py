from django.contrib import admin
from Storage.models import BrandsFood, PetFoods, FoodInventory, StorageTransitions

# Register your models here.


@admin.register(BrandsFood)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ("id", "brand")
    search_fields = ('brand',)


@admin.register(PetFoods)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "weight", "quantity", "quantity_alert", "buy_price", "sell_price_cred", "sell_price_dinh")
    search_fields = ('name', 'weight')


@admin.register(FoodInventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ("id", "all_quantity", "buy_value", "sell_value", "created_at")
    search_fields = ("id", )


@admin.register(StorageTransitions)
class TransitionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'food', 'action', 'quantity', 'date')
    search_fields = ('user', 'date')
