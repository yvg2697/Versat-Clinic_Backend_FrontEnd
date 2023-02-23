from rest_framework import status, viewsets
from rest_framework.response import Response
from apps.trabajador.api.serializer import TrabajadorSerializer

class TrabajadorViewSet(viewsets.ModelViewSet):
    serializer_class = TrabajadorSerializer
    queryset = TrabajadorSerializer.Meta.model.objects.filter()

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter()
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def list(self, request):
        trabajador_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(trabajador_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Trabajador creado con éxito.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            trabajador_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if trabajador_serializer.is_valid():
                trabajador_serializer.save()
                return Response(trabajador_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(trabajador_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        trabajador = self.get_queryset().filter(id=pk).first()
        if trabajador:
            trabajador.delete()
            return Response({'message': 'Trabajador eliminado con éxito.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No existe trabajador con esos datos.'}, status=status.HTTP_400_BAD_REQUEST)