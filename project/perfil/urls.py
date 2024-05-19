from django.urls import path
from .views import index

app_name = 'perfil'

urlpatterns = [
    path('perfil/index', index, name='index')
]