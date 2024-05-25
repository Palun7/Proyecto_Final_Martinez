from django.urls import path
from .views import index, singup, change_password, update_username
from django.contrib.auth.views import LogoutView


app_name= 'login'

urlpatterns = [
    path('login/', index.as_view(template_name='login/index.html'), name='index'),
    path('login/singup', singup, name=('singup')),
    path('login/logout', LogoutView.as_view(template_name='login/logout.html'), name='logout'),
    path('login/update-username', update_username, name='update_username'),
    path('login/update-password', change_password, name='update_password'),
]