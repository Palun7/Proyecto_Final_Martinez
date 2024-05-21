# Generated by Django 5.0.6 on 2024-05-19 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='control',
            options={'verbose_name': 'Control', 'verbose_name_plural': 'Controles'},
        ),
        migrations.AlterField(
            model_name='control',
            name='peso',
            field=models.FloatField(verbose_name='Peso (Kg.)'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='project/static/fotos'),
        ),
    ]