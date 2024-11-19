from django.urls import path
from Bath.views import DailyList, CreatePetDaily

urlpatterns = [
    path('do_dia/', DailyList.as_view(), name="Diario"),
    path('novo_pet/', CreatePetDaily.as_view(), name="novo"),
]


### Novo Plano, Procedimentos, deletar pet, detalhes pet, editar pet