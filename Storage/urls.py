from Storage.views import EstoqueList, EstoqueDetail, CreateFood, UpdateFoodAmount, UpdateFood, DeleteFood
from django.urls import path


urlpatterns = [
    path('', EstoqueList.as_view(), name='home_estoque'),
    path('<int:pk>/', EstoqueDetail.as_view(), name="detail_estoque"),
    path('nova/', CreateFood.as_view(), name='new_food'),
    path('<int:pk>/atualizar/quantidade/', UpdateFoodAmount.as_view(), name="update_food_quantity"),
    path('<int:pk>/atualizar/', UpdateFood.as_view(), name="update_food"),
    path('<int:pk>/deletar/', DeleteFood.as_view(), name="delete_food")
]
