# Generated by Django 4.2.3 on 2023-08-29 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio_app', '0005_paciente_contrasena1_paciente_contrasena2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='contrasena1',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='contrasena2',
        ),
    ]