from django.db.models.signals import pre_save, post_save, post_delete
from django.db.models import Sum, F
from django.dispatch import receiver
from Storage.models import PetFoods, FoodInventory


def CreateInventory():
    count = PetFoods.objects.aggregate(count=Sum('quantity'))['count']
    buy_all_value = PetFoods.objects.aggregate(buy_all_value=Sum(F('quantity') * F('buy_price')))['buy_all_value']
    sel_all_value = PetFoods.objects.aggregate(sell_all_value=Sum(F('quantity') * F('sell_price_cred')))['sell_all_value']

    FoodInventory.objects.create(
        all_quantity=count,
        buy_value=buy_all_value,
        sell_value=sel_all_value
    )


@receiver(pre_save, sender=PetFoods)
def PetsFoods_pre_save(sender, instance, **kwargs):
    if not instance.food_photo:
        instance.food_photo = 'foods/no-photo.png'


@receiver(post_save, sender=PetFoods)
def PetsFoods_post_Save(sender, instance, **kwargs):
    CreateInventory()


@receiver(post_delete, sender=PetFoods)
def PetsFoods_post_delete(sender, instance, **kwargs):
    CreateInventory()
