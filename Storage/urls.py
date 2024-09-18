from Storage.views import estoque_list
from django.urls import path


urlpatterns = [
    path('', estoque_list.as_view(), name='home_estoque'),
]
