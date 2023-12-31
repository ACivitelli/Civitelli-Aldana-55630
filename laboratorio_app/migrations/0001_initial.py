# Generated by Django 4.2.3 on 2023-08-13 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especializacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialización', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estudios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudios', models.CharField(max_length=100)),
                ('estudios_corto', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Profesionales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('matricula', models.DateField()),
            ],
        ),
    ]
