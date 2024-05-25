from django import forms
from .models import Veterinarias, Localidad

class VeterinariasForm(forms.ModelForm):
    class Meta:
        model = Veterinarias
        fields = '__all__'

class LocalidadForm(forms.ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'
