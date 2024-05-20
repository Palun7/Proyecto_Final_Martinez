from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import VacunasForm, MascotaForm, RazaForm, ControlForm
from .models import Mascota, Vacunas, Raza, Control
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from typing import Any
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)


@login_required
def index(request):
    return render(request, 'perfil/index.html', {'user': request.user})

class MascotaCreate(CreateView):
    model = Mascota
    form_class= MascotaForm
    success_url = reverse_lazy('perfil:mascota_list')

class MascotaDetail(DetailView):
    model = Mascota

class MascotaUpdate(UpdateView):
    model = Mascota
    form_class= MascotaForm
    success_url = reverse_lazy('perfil:mascota_list')

class MascotaDelete(DeleteView):
    model = Mascota
    success_url = reverse_lazy('perfil:mascota_list')

class MascotaList(LoginRequiredMixin, ListView):
    model = Mascota
    context_object_name = 'mascotas'
    login_url = 'login/index.html'

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = Mascota.objects.filter(Q(nombre__icontains=busqueda),Q(sexo__icontains=busqueda),Q(raza__icontains=busqueda),Q(color_pelo__icontains=busqueda))
        return queryset

class ControlCreate(CreateView):
    model = Control
    form_class= ControlForm
    success_url = reverse_lazy('perfil:control_list')

class ControlDetail(DetailView):
    model = Control

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacunas'] = self.object.get_vacunas_str() # type: ignore
        return context

class ControlUpdate(UpdateView):
    model = Control
    form_class= ControlForm
    success_url = reverse_lazy('perfil:control_list')

class ControlDelete(DeleteView):
    model = Control
    success_url = reverse_lazy('perfil:control_list')

class ControlList(LoginRequiredMixin, ListView):
    model = Control
    context_object_name = 'controles'
    login_url = 'login/index.html'

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = Control.objects.filter(Q(nombre__icontains=busqueda),Q(peso__icontains=busqueda),Q(vacunas__icontains=busqueda))
        return queryset