from django.db import models
from apps.base.models import BaseModel


# Create your models here.
class Diagnostico(models.Model):
    id = models.AutoField(primary_key=True)
    diagnostico = models.CharField('Diagnóstico', max_length=50, blank=False, null=True)

    class Meta:
        verbose_name = 'Diagnóstico'
        verbose_name_plural = 'Diagnósticos'
        db_table = 'diagnostico'

    def __str__(self):
        return f'{self.diagnostico}'


class APP(models.Model):
    id = models.AutoField(primary_key=True)
    app = models.CharField('Antecedente patológico personal', max_length=50, blank=False, null=True)

    class Meta:
        verbose_name = 'Antecedente patológico personal'
        verbose_name_plural = 'Antecedentes patológicos personales'
        db_table = 'app'

    def __str__(self):
        return f'{self.app}'


class Sala(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Sala', max_length=50, blank=False, null=True)

    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'
        db_table = 'sala'

    def __str__(self):
        return f'{self.nombre}'


class Paciente(BaseModel, models.Model):
    cama = models.CharField('Cama', max_length=255, null=True, blank=False)
    sala = models.ForeignKey('Sala', on_delete=models.CASCADE, verbose_name='Sala', null=True, blank=False)
    diagnostico = models.ForeignKey('Diagnostico', on_delete=models.CASCADE, verbose_name='Diagnóstico', null=False,
                                    blank=False)
    app = models.ForeignKey('APP', on_delete=models.CASCADE, verbose_name='APP', null=False, blank=False)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        db_table = 'paciente'

    REQUIRED_FIELDS = ['cama', 'sala', 'diagnostico', 'app']

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'
