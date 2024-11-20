from django import forms
from Bath.models import AllPets, MonthlyPlans


class DailyPets(forms.ModelForm):
    class Meta:
        model = AllPets
        fields = ['onwer', 'phone', 'pet', 'work', 'race', 'value', 'warnings']


class NewPlan(forms.ModelForm):
    class Meta:
        model = MonthlyPlans
        fields = ['plan_onwer', 'plan_phone', 'plan_pet', 'plan_race', 'value']
        labels = {'plan_onwer':'Nome do dono', 'plan_phone' : 'Nº de Telefone',
                  'plan_pet': 'Nomde do pet', 'plan_race': "Raça do Pet",
                  'value': 'Valor do plano'}