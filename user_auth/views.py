from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,authentication_classes

from .serializers import UserCreateSerializer, LoginSerializer

# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# INFO:: We can create Login and Registration API by APIView's post method as well
# INFO:: But using generics.CreateApiView here to test all the functionalities are working same
class AccountRegistration(generics.CreateAPIView):

    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        errors = None
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            response_data = {
                "message": "User registered successfully",
                "data": serializer.data,
                "token": token,
                "errors": errors
            }
            response_status = status.HTTP_201_CREATED

        else:
            response_data = {
                "data": None,
                "errors": serializer.errors,
            }
            response_status = status.HTTP_400_BAD_REQUEST

        return Response(response_data,status=response_status)


class AccountLogin(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get('username')
            password = serializer.validated_data['password']

            user = authenticate(request, username=username, password=password)

            # DETAILS:: Based on the authenticated user generate the tokens
            token = get_tokens_for_user(user)

            # DETAILS:: Remove the password field from the response data
            response_user_data = serializer.data
            response_user_data.pop('password', None)

            if user is not None:
                response_data = {
                    "message": "logged-in successfully",
                    "data": response_user_data,
                    "token": token,
                    "errors": serializer.errors,
                }
                response_status = status.HTTP_200_OK
            else:
                response_data = {
                    "message": "invalid credentials",
                    "data": response_user_data,
                    "errors": serializer.errors,
                }
                response_status = status.HTTP_404_NOT_FOUND

            return Response(response_data, status=response_status)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)