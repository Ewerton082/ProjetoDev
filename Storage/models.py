from django.db import models

# Create your models here.
WEIGHT_FOODS = ((7.5, "7.5"), (10.1, "10.1"), (14.1, "14.1"), (15.1, "15.1"),
                (18.1, "18.1"), (20.1, "20.1"), (25.1, "25.1"))


class BrandsFood(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(null=False, blank=False, max_length=300)

    def __str__(self):
        return self.brand


class PetFoods(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.ForeignKey(to=BrandsFood, on_delete=models.PROTECT, related_name="brand_food")
    name = models.CharField(blank=False, max_length=500)
    weight = models.FloatField(choices=WEIGHT_FOODS)
    buy_price = models.FloatField(null=True, blank=True)
    sell_price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField()
    quantity_alert = models.IntegerField()
    food_photo = models.ImageField(upload_to="foods/", blank=True, null=True)

    def __str__(self):
        return f"Ração: {self.name} | QTD: {self.quantity}"
