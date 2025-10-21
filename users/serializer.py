from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, ConfirmCode

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_active = False  
        user.save()

        
        code = ConfirmCode.objects.create(user=user, code=ConfirmCode.generate_code())
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Неверное имя пользователя или пароль.")
        if not user.is_active:
            raise serializers.ValidationError("Пользователь не подтверждён.")
        data['user'] = user
        return data

class ConfirmSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        try:
            user = User.objects.get(username=data['username'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Пользователь не найден.")

        if not hasattr(user, 'confirm_code'):
            raise serializers.ValidationError("Код подтверждения не найден.")

        if user.confirm_code.code != data['code']:
            raise serializers.ValidationError("Неверный код подтверждения.")

        user.is_active = True
        user.save()
        user.confirm_code.delete()  
        return data