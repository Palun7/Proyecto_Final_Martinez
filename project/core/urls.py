from django.urls import path
from .views import index, sobre_mi

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('core/sobre_mi', sobre_mi, name='sobre_mi'),
]