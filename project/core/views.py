from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')

def sobre_mi(request):
    return render(request, 'core/sobre_mi.html')