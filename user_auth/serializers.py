from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserCreateSerializer(serializers.ModelSerializer):

    def validate_email(self,value):

        """validate email and it's uniqueness"""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def create(self, validated_data):

        # same functionalities we will get
        # below is a one way of creating users
        # validated_data["password"] = make_password(validated_data["password"])
        # user = User.objects.create(**validated_data)
        # UserProfile.objects.create(user=user)
        print(validated_data["email"])
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user)

        return user

    class Meta:
        model = User
        fields = ["username","email","password"]


class LoginSerializer(serializers.Serializer):
    password = serializers.CharField()
    username = serializers.CharField()

    class Meta:
        model = User
        fields = "__all__"

