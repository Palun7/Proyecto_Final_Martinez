from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from .forms import VeterinariasForm, LocalidadForm, TipoAnimalForm, TipCuriosidadForm
from .models import Veterinarias, Localidad, TipoAnimal, TipCuriosidad
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q



def index(request):
    return render(request, 'comunidad/index.html')

class VeterinariasCreate(CreateView, LoginRequiredMixin):
    model = Veterinarias
    form_class= VeterinariasForm
    success_url = reverse_lazy('comunidad:veterinarias_list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class VeterinariasDetail(DetailView):
    model = Veterinarias

class VeterinariasUpdate(UpdateView, LoginRequiredMixin):
    model = Veterinarias
    form_class= VeterinariasForm
    success_url = reverse_lazy('comunidad:veterinarias_list')

class VeterinariasDelete(DeleteView, LoginRequiredMixin):
    model = Veterinarias
    success_url = reverse_lazy('comunidad:veterinarias_list')

def veterinariaslist(request):
    busqueda = request.GET.get("busqueda", None)
    consulta = Veterinarias.objects.all()
    if busqueda:
        consulta = Veterinarias.objects.filter(
            Q(nombre__icontains=busqueda) |
            Q(direccion__icontains=busqueda) |
            Q(localidad__localidad__icontains=busqueda)
            )
        contexto = {
            'veterinarias': consulta,
            'user' : request.user
        }
    else:
        consulta = Veterinarias.objects.all()
        contexto = {
            'veterinarias': consulta,
            'user' : request.user
        }
    return render(request, 'comunidad/veterinarias_list.html', contexto)

class LocalidadCreate(CreateView):
    model = Localidad
    form_class= LocalidadForm
    success_url = reverse_lazy('comunidad:veterinarias_create')

class TipoAnimalCreate(CreateView):
    model = TipoAnimal
    form_class = TipoAnimalForm
    success_url = reverse_lazy('comunidad:tipcuriosidad_create')

class TipCuriosidadCreate(CreateView, LoginRequiredMixin):
    model = TipCuriosidad
    form_class = TipCuriosidadForm
    success_url = reverse_lazy('comunidad:tipcuriosidad_list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class TipCuriosidadDetail(DetailView):
    model = TipCuriosidad

class TipCuriosidadUpdate(UpdateView, LoginRequiredMixin):
    model = TipCuriosidad
    form_class= TipCuriosidadForm
    success_url = reverse_lazy('comunidad:tipcuriosidad_list')

class TipCuriosidadDelete(DeleteView, LoginRequiredMixin):
    model = TipCuriosidad
    success_url = reverse_lazy('comunidad:tipcuriosidad_list')

def tipcuriosidadlist(request):
    busqueda = request.GET.get("busqueda", None)
    consulta = TipCuriosidad.objects.all()
    if busqueda:
        consulta = TipCuriosidad.objects.filter(
            Q(nombre__icontains=busqueda) |
            Q(animal__nombre__icontains=busqueda) |
            Q(tip_o_curiosidad__icontains=busqueda)
            )
        contexto = {
            'tipcuriosidad': consulta,
            'user' : request.user
        }
    else:
        consulta = TipCuriosidad.objects.all()
        contexto = {
            'tipcuriosidad': consulta,
            'user' : request.user
        }
    return render(request, 'comunidad/tipcuriosidad_list.html', contexto)