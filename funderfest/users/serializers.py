from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
            model = CustomUser
            fields ='__all__'
            extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        instance.password = validated_data.get('password', instance.password)
        instance.last_login = validated_data.get('last_login',instance.last_login)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.date_joined = validated_data.get('date_joined', instance.date_joined)
        instance.save()
        return instance