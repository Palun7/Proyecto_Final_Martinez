# Generated by Django 5.0.4 on 2024-05-21 02:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0009_alter_control_vacunas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='control',
            name='ultima_visita_veterinario',
        ),
        migrations.AddField(
            model_name='control',
            name='fecha_control',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]