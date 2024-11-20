from django.urls import path
from Bath.views import DailyList, CreatePetDaily, CreateNewPlan

urlpatterns = [
    path('do_dia/', DailyList.as_view(), name="Diario"), #Listagem dos pets Diarios
    path('novo_pet/', CreatePetDaily.as_view(), name="novo"), #Adicionar novo Pet Diario
    path('novo_plano/', CreateNewPlan.as_view(), name="novo_plano"), #novo plano
]


### Novo Plano, Procedimentos, deletar pet, detalhes pet, editar pet  [Mais importante: Realizar Relatorio de data definidia por usuario xx/xx/xxxx até xx/xx/xxxx ]