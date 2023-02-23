from django.contrib import admin
from .models import Trabajador, Categoria_Ocupacional, Grado_Cientifico

# Register your models here.
admin.site.register(Trabajador)
admin.site.register(Categoria_Ocupacional)
admin.site.register(Grado_Cientifico)
