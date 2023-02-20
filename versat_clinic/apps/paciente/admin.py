from django.contrib import admin
from apps.paciente.models import Diagnostico, Paciente, APP, Sala

# Register your models here.
admin.site.register(Diagnostico)
admin.site.register(Paciente)
admin.site.register(APP)
admin.site.register(Sala)