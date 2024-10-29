from django import forms
from Bath.models import AllPets


class DailyPets(forms.ModelForm):
    class Meta:
        model = AllPets
        fields = ['onwer', 'phone', 'pet', 'work', 'race', 'value', 'warnings']

        