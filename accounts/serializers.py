from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'role']

    def create(self, validated_data):
        role = validated_data.get('role', 'trainer')
        if role == 'admin':
            validated_data['is_staff'] = True
            validated_data['is_superuser'] = True

        password = validated_data.pop('password')
        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
