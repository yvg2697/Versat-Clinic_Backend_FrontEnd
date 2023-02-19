from django.db import models

# Create your models here.
class Sexo(models.Model):
    id = models.AutoField(primary_key=True)
    sexo = models.CharField('Sexo', max_length=50, blank=False, null=True)

    class Meta:
        verbose_name = 'Sexo'
        verbose_name_plural = 'Sexos'
        db_table = 'sexo'

    def __str__(self):
        return f'{self.sexo}'


class Raza(models.Model):
    id = models.AutoField(primary_key=True)
    raza = models.CharField('Raza', max_length=50, blank=False, null=True)

    class Meta:
        verbose_name = 'Raza'
        verbose_name_plural = 'Razas'
        db_table = 'raza'

    def __str__(self):
        return f'{self.raza}'


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=255, blank=False, null=False)
    apellidos = models.CharField('Apellidos', max_length=255, blank=False, null=False)
    email = models.EmailField('Correo Electrónico', max_length=255, blank=True, null=True)
    municipio = models.CharField('Municipio', max_length=100, blank=True, null=True)
    provincia = models.CharField('Provincia', max_length=100, blank=True, null=True)
    pais = models.CharField('País', max_length=100, blank=True, null=True)
    direccion = models.CharField('Dirección', max_length=250, blank=True, null=True)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE, verbose_name='Sexo', null=False, blank=False)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE, verbose_name='Raza', null=False, blank=False)
    imagen = models.ImageField('Imagen de perfil', upload_to='pefil/', max_length=255, blank=True, null=True)

    class Meta:
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'

    REQUIRED_FIELDS = ['nombre','apellidos', 'municipio', 'provincia', 'pais', 'direccion', 'raza', 'sexo']