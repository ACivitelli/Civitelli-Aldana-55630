# Generated by Django 4.2.3 on 2023-08-31 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio_app', '0010_alter_preguntasfrecuentes_respuesta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudios',
            name='estudios',
        ),
        migrations.RemoveField(
            model_name='estudios',
            name='estudios_corto',
        ),
        migrations.AddField(
            model_name='estudios',
            name='prestacion',
            field=models.CharField(default=1, max_length=800),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estudios',
            name='valor',
            field=models.IntegerField(null=1),
            preserve_default=1,
        ),
    ]
