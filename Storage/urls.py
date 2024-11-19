from Storage.views import EstoqueList, EstoqueDetail, CreateFood, UpdateFoodAmount, UpdateFood, DeleteFood, CreateBrand
from django.urls import path


urlpatterns = [
    path('', EstoqueList.as_view(), name='home_estoque'), #Listagem
    path('<int:pk>/', EstoqueDetail.as_view(), name="detail_estoque"), #Detalhes de Produto
    path('nova/', CreateFood.as_view(), name='new_food'), #Nova Ração
    path('nova_brand/', CreateBrand.as_view(), name="new_brand"), #Nova Marca
    path('<int:pk>/atualizar/quantidade/', UpdateFoodAmount.as_view(), name="update_food_quantity"), #Realizar vendas ou compras
    path('<int:pk>/atualizar/', UpdateFood.as_view(), name="update_food"), # Editar Detalhes da Ração
    path('<int:pk>/deletar/', DeleteFood.as_view(), name="delete_food") # Deletar Rações
]
