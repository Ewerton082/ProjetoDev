from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from Storage.models import PetFoods, StorageTransitions
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
    fields = ['animal', 'brand', 'name', 'weight',
              'buy_price', 'sell_price', 'quantity_alert',
              'food_photo']
    template_name = 'food_update.html'

    def get_success_url(self):
        return reverse_lazy('detail_estoque', kwargs={'pk': self.object.pk})


class DeleteFood(DeleteView):
    model = PetFoods
    template_name = "delete_food.html"
    success_url = reverse_lazy('home_estoque')


class UpdateFoodAmount(UpdateView):
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
                self.create_transition('venda', food_item, quantity)

        if action == 'compra':
            food_item.quantity += quantity
            self.create_transition('compra', food_item, quantity)

        food_item.save()

        messages.success(self.request, "Dados salvos com sucesso")
        return redirect(self.get_success_url(food_item.pk))

    def create_transition(self, action_type, food_item, quantity_item):
        StorageTransitions.objects.create(
            user=self.request.user,
            food=food_item,
            quantity=quantity_item,
            action=action_type
        )

    def get_success_url(self, pk):
        return reverse_lazy('detail_estoque', kwargs={'pk': pk})
