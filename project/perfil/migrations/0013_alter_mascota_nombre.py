# Generated by Django 5.0.4 on 2024-05-21 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0012_alter_mascota_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
    ]