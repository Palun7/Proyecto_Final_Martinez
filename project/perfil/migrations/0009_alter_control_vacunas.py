# Generated by Django 5.0.4 on 2024-05-20 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0008_alter_control_peso_alter_control_vacunas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='control',
            name='vacunas',
            field=models.ManyToManyField(to='perfil.vacunas'),
        ),
    ]
