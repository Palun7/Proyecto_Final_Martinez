from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm, CustomUserCreationForm, UpdateUsernameForm, CustomPasswordChangeForm
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


class index(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "login/index.html"

def singup(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "login/singup.html", {"mensaje": f"Pawsuario '{username}', fue registrado con éxito."})
    else:
        form = CustomUserCreationForm()
    return render(request, "login/singup.html", {"form": form})

@login_required
def update_username(request):
    if request.method == 'POST':
        form = UpdateUsernameForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu nombre de usuario se cambió con éxito.')
            return redirect('perfil:index')
    else:
        form = UpdateUsernameForm(instance=request.user)
    return render(request, 'login/update_username.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Tu contraseña se actualizó con éxito.')
            return redirect('perfil:index')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'login/change_password.html', {'form': form})