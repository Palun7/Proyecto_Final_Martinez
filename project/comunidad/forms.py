from django import forms
from .models import Veterinarias, Localidad, TipoAnimal, TipCuriosidad

class VeterinariasForm(forms.ModelForm):
    class Meta:
        model = Veterinarias
        fields = ['nombre', 'telefono', 'direccion', 'localidad', 'ubicacion', 'foto_referencia', 'descripcion']

class LocalidadForm(forms.ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'

class TipoAnimalForm(forms.ModelForm):
    class Meta:
        model = TipoAnimal
        fields = '__all__'

class TipCuriosidadForm(forms.ModelForm):
    class Meta:
        model = TipCuriosidad
        fields = ['nombre', 'animal', 'tip_o_curiosidad', 'url', 'dato']
