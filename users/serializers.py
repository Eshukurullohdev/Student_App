from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'phone', 'password', 'role')

    def create(self, validated_data):
        user = User(
            phone=validated_data['phone'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user



from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            phone=data['phone'],
            password=data['password']
        )
        if not user:
            raise serializers.ValidationError("Telefon yoki parol noto‘g‘ri")
        return user
