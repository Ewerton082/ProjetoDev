from django.db import models

# Create your models here.


class StandartWorks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


class AllPets(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    onwer = models.CharField(max_length=200, null=False, blank=False)
    phone = models.CharField(max_length=16, null=False, blank=False)
    pet = models.CharField(max_length=200, blank=True, null=True)
    work = models.ForeignKey(to=StandartWorks, on_delete=models.PROTECT, related_name="procedimentos")
    race = models.CharField(max_length=200, null=True, blank=True)
    value = models.FloatField(blank=True, null=True)
    warnings = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f'{self.onwer}|{self.pet} | {self.work}'

    class Meta:
        ordering = ['-date']


class MonthlyPlans(models.Model):
    plan_onwer = models.CharField(max_length=200, null=False, blank=False)
    plan_phone = models.CharField(max_length=16, null=False, blank=False)
    plan_pet = models.CharField(max_length=200, null=False, blank=False)
    plan_race = models.CharField(max_length=200, null=False, blank=False)
    bath1 = models.DateField(blank=True, null=True)
    bath2 = models.DateField(blank=True, null=True)
    bath3 = models.DateField(blank=True, null=True)
    bath4 = models.DateField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
