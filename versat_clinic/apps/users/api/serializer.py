from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username,
            'name': instance.name,
            'last_name': instance.last_name,
            'email': instance.email,
        }


# Serializador para el Login
class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name')
