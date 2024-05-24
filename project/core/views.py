from django.shortcuts import render
from perfil.models import Mascota


def index(request):
    return render(request, 'core/index.html')

def sobre_mi(request):
    return render(request, 'core/sobre_mi.html')

def galeria_fotos(request):
    mascotas = Mascota.objects.all()
    context = {
        'mascotas': mascotas,
    }
    return render(request, 'core/galeria_fotos.html', context)