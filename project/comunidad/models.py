from django.db import models

class Localidad(models.Model):
    localidad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.localidad} ({self.provincia})'

    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'

class Veterinarias(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, verbose_name='teléfono')
    direccion = models.CharField(max_length=150, verbose_name='dirección')
    localidad = models.ForeignKey(Localidad, on_delete=models.SET_NULL, null=True,blank=True)
    ubicacion = models.CharField(max_length=250, null=True,blank=True, verbose_name='ubicación')
    foto_referencia = models.ImageField(upload_to='fotos',null=True,blank=True)
    descripcion = models.TextField(null=True,blank=True, verbose_name='descripción')

    def __str__(self):
        return f'{self.nombre}, {self.localidad}'

    class Meta:
        verbose_name = 'Veterinaria'
        verbose_name_plural = 'Veterinarias'
