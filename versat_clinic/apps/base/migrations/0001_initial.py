# Generated by Django 4.1.7 on 2023-02-19 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('raza', models.CharField(max_length=50, null=True, verbose_name='Raza')),
            ],
            options={
                'verbose_name': 'Raza',
                'verbose_name_plural': 'Razas',
                'db_table': 'raza',
            },
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sexo', models.CharField(max_length=50, null=True, verbose_name='Sexo')),
            ],
            options={
                'verbose_name': 'Sexo',
                'verbose_name_plural': 'Sexos',
                'db_table': 'sexo',
            },
        ),
    ]
