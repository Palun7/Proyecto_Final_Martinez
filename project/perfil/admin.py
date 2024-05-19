from django.contrib import admin
from .models import Mascota, Vacunas, Raza, Control

admin.site.register(Mascota)
admin.site.register(Vacunas)
admin.site.register(Raza)
admin.site.register(Control)