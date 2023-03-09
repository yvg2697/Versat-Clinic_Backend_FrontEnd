from django.db import models
from apps.base.models import BaseModel


class Categoria_Ocupacional(models.Model):
    id = models.AutoField(primary_key=True)
    categoria_ocupacional = models.CharField('Categoría ocupacional', max_length=50, blank=False, null=True)

    class Meta:
        verbose_name = 'Categoria ocupacional'
        verbose_name_plural = 'Categorías ocupacionales'
        db_table = 'categoria_ocupacional'

    def __str__(self):
        return f'{self.categoria_ocupacional}'


class Grado_Cientifico(models.Model):
    id = models.AutoField(primary_key=True)
    grado_cientifico = models.CharField('Grado científico', max_length=50, blank=False, null=True)

    class Meta:
        verbose_name = 'Grado científico'
        verbose_name_plural = 'Grados científicos'
        db_table = 'grado_cientifico'

    def __str__(self):
        return f'{self.grado_cientifico}'


class Trabajador(BaseModel):
    local = models.CharField('Local de trabajo', max_length=255, null=True, blank=False)
    categoria_ocupacional = models.ForeignKey(Categoria_Ocupacional, on_delete=models.CASCADE,
                                              verbose_name='Categoría ocupacional', null=False, blank=False)
    grado_cientifico = models.ForeignKey(Grado_Cientifico, on_delete=models.CASCADE, verbose_name='Grado científico',
                                         null=False, blank=False)

    class Meta:
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadores'
        db_table = 'trabajador'

    REQUIRED_FIELDS = ['categoria_ocupacional', 'grado_cientifico']

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'
