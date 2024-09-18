from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from Storage.models import PetFoods


# Create your views here.


class estoque_list(ListView):
    template_name = "estoque_list.html"
    model = PetFoods
    context_object_name = "food"