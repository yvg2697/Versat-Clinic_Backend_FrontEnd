from rest_framework import serializers

from versat_clinic.apps.paciente.models import Paciente


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'
