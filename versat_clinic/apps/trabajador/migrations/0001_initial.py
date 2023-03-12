# Generated by Django 4.1.7 on 2023-03-12 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria_Ocupacional',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('categoria_ocupacional', models.CharField(max_length=50, null=True, verbose_name='Categoría ocupacional')),
            ],
            options={
                'verbose_name': 'Categoria ocupacional',
                'verbose_name_plural': 'Categorías ocupacionales',
                'db_table': 'categoria_ocupacional',
            },
        ),
        migrations.CreateModel(
            name='Grado_Cientifico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('grado_cientifico', models.CharField(max_length=50, null=True, verbose_name='Grado científico')),
            ],
            options={
                'verbose_name': 'Grado científico',
                'verbose_name_plural': 'Grados científicos',
                'db_table': 'grado_cientifico',
            },
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=255, verbose_name='Apellidos')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Correo Electrónico')),
                ('municipio', models.CharField(blank=True, max_length=100, null=True, verbose_name='Municipio')),
                ('provincia', models.CharField(blank=True, max_length=100, null=True, verbose_name='Provincia')),
                ('pais', models.CharField(blank=True, max_length=100, null=True, verbose_name='País')),
                ('direccion', models.CharField(blank=True, max_length=250, null=True, verbose_name='Dirección')),
                ('imagen', models.ImageField(blank=True, max_length=255, null=True, upload_to='pefil/', verbose_name='Imagen de perfil')),
                ('local', models.CharField(max_length=255, null=True, verbose_name='Local de trabajo')),
                ('categoria_ocupacional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajador.categoria_ocupacional', verbose_name='Categoría ocupacional')),
                ('grado_cientifico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajador.grado_cientifico', verbose_name='Grado científico')),
                ('raza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.raza', verbose_name='Raza')),
                ('sexo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.sexo', verbose_name='Sexo')),
            ],
            options={
                'verbose_name': 'Trabajador',
                'verbose_name_plural': 'Trabajadores',
                'db_table': 'trabajador',
            },
        ),
    ]
