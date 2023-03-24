from rest_framework import status, viewsets
from rest_framework.response import Response

from apps.paciente.api.serializer import PacienteSerializer
from apps.users.authentication_mixin import Authentication


class PacienteViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = PacienteSerializer
    queryset = PacienteSerializer.Meta.model.objects.filter()

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter()
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def list(self, request):
        paciente_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(paciente_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Paciente creado con éxito.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            paciente_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if paciente_serializer.is_valid():
                paciente_serializer.save()
                return Response(paciente_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(paciente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        paciente = self.get_queryset().filter(id=pk).first()
        if paciente:
            paciente.delete()
            return Response({'message': ' Paciente eliminado con éxito.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No existe paciente con esos datos.'}, status=status.HTTP_400_BAD_REQUEST)
