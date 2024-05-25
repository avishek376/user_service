from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserCreateSerializer(serializers.ModelSerializer):

    def validate_email(self,value):
        # DETAILS:: validate email and it's uniqueness

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def create(self, validated_data):

        # DETAILS:: Below is also a way to create users
        # validated_data["password"] = make_password(validated_data["password"])
        # user = User.objects.create(**validated_data)
        # UserProfile.objects.create(user=user)

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

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["first_name","last_name","username"]


class UserProfileViewSerializer(serializers.ModelSerializer):
    """serializer for user profile to view as user-profile or user-list"""

    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id","first_name","last_name","username","email","role"]

    def get_role(self, obj):
        return obj.userprofile.role if hasattr(obj, 'userprofile') else None