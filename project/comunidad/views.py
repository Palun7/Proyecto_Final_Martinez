from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from .forms import VeterinariasForm, LocalidadForm
from .models import Veterinarias, Localidad
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q



def index(request):
    return render(request, 'comunidad/index.html')

class VeterinariasCreate(CreateView, LoginRequiredMixin):
    model = Veterinarias
    form_class= VeterinariasForm
    success_url = reverse_lazy('comunidad:veterinarias_list')

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
    else:
        consulta = Veterinarias.objects.all()
    return render(request, 'comunidad/veterinarias_list.html', {'veterinarias': consulta})
    
class LocalidadCreate(CreateView):
    model = Localidad
    form_class= LocalidadForm
    success_url = reverse_lazy('comunidad:veterinarias_create')