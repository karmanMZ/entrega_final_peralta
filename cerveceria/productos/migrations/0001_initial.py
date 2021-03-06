# Generated by Django 4.0.4 on 2022-06-19 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cerv_art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estilo', models.CharField(max_length=40)),
                ('ibu', models.IntegerField()),
                ('alcohol', models.IntegerField()),
                ('cuerpo', models.CharField(max_length=40)),
                ('amargor', models.CharField(max_length=40)),
                ('aroma', models.CharField(max_length=40)),
                ('temp_consumo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=40)),
                ('tipo_producto', models.CharField(max_length=40)),
                ('fecha_registro', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Vino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=40)),
                ('estado', models.CharField(max_length=40)),
                ('envejecimiento', models.IntegerField()),
                ('calidad', models.CharField(max_length=40)),
                ('azucar', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Whisky',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=40)),
                ('materia_prima', models.CharField(max_length=40)),
                ('destilacion', models.CharField(max_length=40)),
                ('tipo_agua', models.CharField(max_length=40)),
                ('tiempo', models.IntegerField()),
            ],
        ),
    ]
