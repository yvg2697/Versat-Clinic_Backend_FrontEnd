from rest_framework import serializers
from apps.trabajador.models import Trabajador

class TrabajadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trabajador
        fields = '__all__'