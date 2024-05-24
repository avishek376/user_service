from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import MD5PasswordHasher

class UserCreateSerializer(serializers.ModelSerializer):

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user)

        return user

    class Meta:
        model = User
        fields = ["username","email","password"]


class LoginSerializer(serializers.Serializer):
    password = serializers.CharField()
    username = serializers.CharField()

    # class Meta:
    #     model = User
    #     fields = "__all__"

