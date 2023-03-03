from django.contrib import admin
from versat_clinic.apps.paciente.models import Diagnostico, Paciente, APP, Sala

# Register your models here.
admin.site.register(Diagnostico)
admin.site.register(Paciente)
admin.site.register(APP)
admin.site.register(Sala)
