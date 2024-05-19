from django import forms
from .models import Control, Vacunas, Mascota, Raza

class ControlForm(forms.ModelForm):
    class Meta:
        model = Control
        fields = '__all__'

class VacunasForm(forms.ModelForm):
    class Meta:
        model = Vacunas
        fields = '__all__'

class MascotaForm(forms.ModelForm):
    class Meta:
        model= Mascota
        fields = '__all__'

class RazaForm(forms.ModelForm):
    class Meta:
        model = Raza
        fields = '__all__'