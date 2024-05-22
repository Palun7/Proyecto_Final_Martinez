from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Raza(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Raza'
        verbose_name_plural = 'Razas'

class Vacunas(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Vacuna'
        verbose_name_plural = 'Vacunas'


class Mascota(models.Model):
    nombre= models.CharField(max_length=50, verbose_name='Nombre')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    sexo = models.CharField(max_length=20, null=True, blank=True, verbose_name='Sexo')
    raza = models.ForeignKey(Raza, on_delete=models.SET_NULL,null=True, blank=True, verbose_name='Raza')
    color_pelo = models.CharField(max_length=100, null=True,blank=True, verbose_name='Color de pelo')
    foto = models.ImageField(upload_to='fotos',null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True, verbose_name=('Descripción'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def edad(self):
        today = date.today()
        edad = today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return edad

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'

class Control(models.Model):
    nombre = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    peso = models.FloatField(verbose_name='Peso (Kg.)', null=True, blank=True)
    vacunas = models.ManyToManyField(Vacunas)
    fecha_control = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre}, Fecha control: {self.fecha_control.day}/{self.fecha_control.month}/{self.fecha_control.year}.'

    def get_vacunas_str(self):
        return ' / '.join([vacuna.nombre for vacuna in self.vacunas.all()])

    class Meta:
        verbose_name = 'Control'
        verbose_name_plural = 'Controles'