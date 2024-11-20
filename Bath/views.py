from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from Bath.models import AllPets, MonthlyPlans, StandartWorks
from Bath.forms import DailyPets, NewPlan
import datetime
# Create your views here.


class DailyList(ListView):
    template_name = "do_dia_list.html"
    model = AllPets
    context_object_name = "pets"


    def get_queryset(self):
        query = super().get_queryset()
        date_filter = self.request.GET.get('date_filter')
        data_hoje = str(datetime.date.today())
        
        if date_filter:
            query = query.filter(date=date_filter)
        
        else:
            query = query.filter(date=data_hoje)
        return query
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['planos'] = MonthlyPlans.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        selected_plan = self.request.POST.get('planos_mensais')
        if selected_plan:
            montly = MonthlyPlans.objects.get(id=selected_plan)

            new_pet = AllPets(
                onwer=montly.plan_onwer,
                phone=montly.plan_phone,
                pet=montly.plan_pet,
                work= StandartWorks.objects.get(id=1),
                race=montly.plan_race,
            )
            new_pet.save()
        return redirect('Diario')


class CreatePetDaily(CreateView):
    form_class = DailyPets
    model = AllPets
    success_url = reverse_lazy('Diario')
    template_name = "novo_pet_diario.html"


class CreateNewPlan(CreateView):
    form_class = NewPlan
    model = MonthlyPlans
    success_url = reverse_lazy('Diario')
    template_name = "novo_plano_pet.html"
    
    