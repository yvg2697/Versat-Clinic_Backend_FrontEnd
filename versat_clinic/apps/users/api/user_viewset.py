from rest_framework import status, viewsets
from rest_framework.response import Response
from apps.users.authentication_mixin import Authentication

from apps.users.api.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.filter()

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter()
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def list(self, request):
        user_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Usuario creado con éxito.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            user_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user = self.get_queryset().filter(id=pk).first()
        if user:
            user.delete()
            return Response({'message': 'Usuario eliminado con éxito.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No existe usuario con esos datos.'})
