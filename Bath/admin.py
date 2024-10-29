from django.contrib import admin
from Bath.models import AllPets, MonthlyPlans, StandartWorks

# Register your models here.


@admin.register(StandartWorks)
class WorksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(AllPets)
class AllPetsAdmin(admin.ModelAdmin):
    list_display = ('date', 'onwer', 'phone', 'pet', 'race', 'work', 'value')
    search_fields = ('onwer', 'pet')


@admin.register(MonthlyPlans)
class PlansAdmin(admin.ModelAdmin):
    list_display = ('plan_onwer', 'plan_pet', 'plan_race', 'value', 'bath1', 'bath2', 'bath3', 'bath4')
    search_fields = ('plan_onwer', 'plan_pet')
