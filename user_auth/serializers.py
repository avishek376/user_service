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


class UserChangePasswordSerializer(serializers.Serializer):
    # email = serializers.EmailField()
    old_password = serializers.CharField(max_length=12, write_only=True, required=True, help_text='Old password')
    new_password = serializers.CharField(max_length=12, write_only=True, required=True, help_text='New password')

    class Meta:
        fields = ['old_password','new_password']

    def validate_new_password(self, value):
        # DETAILS:: Validate the password
        special_char = "!@#$%^&*()_+"

        if len(value) < 6:
            raise serializers.ValidationError("Password must be at least 6 characters long")

        if len(value) > 10:
            raise serializers.ValidationError("Password must not be 10 characters long")

        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("Password must contain at least one numeric character")

        if not any(char.isupper() for char in value):
            raise serializers.ValidationError("Password must be at least one uppercase letter")

        if not any(char.islower() for char in value):
            raise serializers.ValidationError("Password must be at least one lowercase letter")

        if not any(char in special_char for char in value):
            raise serializers.ValidationError("Password must be at least one special character")

        return value

    def validate(self, data):
        # DETAILS:: Validate the old password and new password
        if data['old_password'] == data['new_password']:
            raise serializers.ValidationError("New password can't be same as old password")

        # DETAILS:: Extracting the user that is passed in the context
        user = self.context.get('user')

        # DETAILS:: Check if the old password is correct
        if not user.check_password(data['old_password']):
            raise serializers.ValidationError("Old password is incorrect")
        user.set_password(data['new_password'])
        user.save()

        return data

