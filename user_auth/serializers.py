from rest_framework import serializers
from .models import User




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_code', 'phone_number', 'gender', 'country']



class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_code', 'phone_number', 'gender', 'country', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create_user(password=password, **validated_data)
        return user

