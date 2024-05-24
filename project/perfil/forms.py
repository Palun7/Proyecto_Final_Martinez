from django import forms
from .models import Control, Vacunas, Mascota, Raza

class ControlForm(forms.ModelForm):
    class Meta:
        model = Control
        fields = ['nombre', 'peso', 'vacunas', 'castrado', 'otras_intervenciones', 'descripcion']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['nombre'].queryset = Mascota.objects.filter(user=user)

class VacunasForm(forms.ModelForm):
    class Meta:
        model = Vacunas
        fields = '__all__'

class MascotaForm(forms.ModelForm):
    class Meta:
        model= Mascota
        fields = ['nombre', 'fecha_nacimiento', 'sexo', 'raza', 'color_pelo', 'alimento', 'datos_importantes', 'foto', 'descripcion']

class RazaForm(forms.ModelForm):
    class Meta:
        model = Raza
        fields = '__all__'