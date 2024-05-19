from django.urls import path
from .views import index, singup
from django.contrib.auth.views import LogoutView


app_name= 'login'

urlpatterns = [
    path('login/index', index.as_view(template_name='login/index.html'), name='index'),
    path('login/singup', singup, name=('singup')),
    path('login/logout', LogoutView.as_view(template_name='login/logout.html'), name='logout')
]