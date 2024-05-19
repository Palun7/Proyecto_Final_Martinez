from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.http import HttpRequest, HttpResponse



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