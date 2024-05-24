from django.urls import path
from .views import index, sobre_mi, galeria_fotos

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('core/sobre_mi', sobre_mi, name='sobre_mi'),
    path('core/galeria_fotos', galeria_fotos, name='galeria_fotos'),
]