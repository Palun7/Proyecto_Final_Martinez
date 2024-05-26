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

class TipoAnimal(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'animal'
        verbose_name_plural = 'animales'

class TipCuriosidad(models.Model):

    class TipoCuriosidad(models.TextChoices):
        TIP = 'tip', 'Tip'
        CURIOSIDAD = 'curiosidad', 'Curiosidad'

    nombre = models.CharField(max_length=100)
    animal = models.ForeignKey(TipoAnimal, on_delete=models.SET_NULL, null=True, blank=True)
    tip_o_curiosidad = models.CharField(max_length=10, choices=TipoCuriosidad.choices, verbose_name='Tip o curiosidad')
    url = models.CharField(max_length=250,null=True,blank=True, verbose_name='URL')
    dato = models.TextField(null=True,blank=True)

    def __str__(self):
        return f'{self.nombre}, {self.animal}'

    class Meta:
        verbose_name = 'Tip o curiosidad'
        verbose_name_plural = 'Tips o curiosidades'