from Storage.views import EstoqueList, EstoqueDetail, CreateFood, UpdateFood
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', EstoqueList.as_view(), name='home_estoque'),
    path('<int:pk>/', EstoqueDetail.as_view(), name="detail_estoque"),
    path('nova/', CreateFood.as_view(), name='new_food'),
    path('<int:pk>/atualizar/', UpdateFood.as_view(), name="update_food"),
]
