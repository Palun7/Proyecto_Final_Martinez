# Generated by Django 5.0.4 on 2024-05-25 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunidad', '0002_veterinarias_telefono_alter_veterinarias_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veterinarias',
            name='telefono',
            field=models.CharField(default='-', max_length=15, verbose_name='teléfono'),
        ),
    ]
