from django.db import models
from django.contrib.auth.models import User

# Create your models here.
WEIGHT_FOODS = ((7.5, "7.5"), (10.1, "10.1"), (14.1, "14.1"), (15.1, "15.1"),
                (18.1, "18.1"), (20.1, "20.1"), (25.1, "25.1"))

ANIMAL_CHOICES = (("dog", "Cão"), ("cat", "Gato"))


class BrandsFood(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(null=False, blank=False, max_length=300)

    def __str__(self):
        return self.brand


class PetFoods(models.Model):
    id = models.AutoField(primary_key=True)
    animal = models.CharField(choices=ANIMAL_CHOICES, max_length=5)
    brand = models.ForeignKey(to=BrandsFood, on_delete=models.PROTECT, related_name="brand_food")
    name = models.CharField(blank=False, max_length=500)
    weight = models.FloatField(choices=WEIGHT_FOODS)
    buy_price = models.FloatField(null=True, blank=True)
    sell_price_cred = models.FloatField(null=True, blank=True)
    sell_price_dinh = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField()
    quantity_alert = models.IntegerField()
    food_photo = models.ImageField(upload_to="foods/", blank=True, null=True)

    def __str__(self):
        return f"Ração: {self.name}"


class FoodInventory(models.Model):
    id = models.AutoField(primary_key=True)
    all_quantity = models.IntegerField(null=False, blank=False)
    buy_value = models.FloatField(null=False, blank=False)
    sell_value = models.FloatField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.created_at} | {self.all_quantity} Rações no valor total de compra {self.buy_value} e de venda de {self.sell_value}'

    class Meta:
        ordering = ['-created_at']


class StorageTransitions(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    food = models.ForeignKey(to=PetFoods, on_delete=models.CASCADE)
    action = models.CharField(max_length=30, null=True, blank=True)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Realizou uma {self.action} de {self.quantity} {self.food.name} | {self.date}'
