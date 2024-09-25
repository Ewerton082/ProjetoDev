from django.forms import BaseModelForm
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from Storage.models import PetFoods
from django.contrib import messages


# Create your views here.


class EstoqueList(ListView):
    template_name = "estoque_list.html"
    model = PetFoods
    context_object_name = "food"


class EstoqueDetail(DetailView):
    template_name = "estoque_detail.html"
    model = PetFoods
    context_object_name = "food"


class CreateFood(CreateView):
    template_name = "food_create.html"
    model = PetFoods
    template_name_suffix = 'food'
    fields = "__all__"
    success_url = "../"


class UpdateFood(UpdateView):
    model = PetFoods
    fields = []

    def form_valid(self, form):
        food_item = form.save(commit=False)

        action = self.request.POST.get('action_type')
        quantity = int(self.request.POST.get('amount'))

        if action == 'venda':
            if food_item.quantity - quantity < 0:
                messages.error(self.request, "Não Temos essa quantidade em nosso estoque")
                return redirect(self.get_success_url(food_item.pk))

            else:
                food_item.quantity -= quantity
        
        if action == 'compra':
            food_item.quantity += quantity
        
        food_item.save()
        
        messages.success(self.request, "Dados salvos com sucesso")
        return redirect(self.get_success_url(food_item.pk))
    
    def get_success_url(self, pk):
        return reverse_lazy('detail_estoque', kwargs ={'pk':pk})