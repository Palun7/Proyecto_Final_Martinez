# Generated by Django 5.0.4 on 2024-05-20 22:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0006_alter_control_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='control',
            name='nombre',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='perfil.mascota'),
        ),
    ]
