from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import generics,mixins
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,authentication_classes
from .models import User,UserProfile
from .serializers import UserCreateSerializer, LoginSerializer

# Create your views here.


class AccountRegistration(generics.CreateAPIView):

    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        errors = None
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response_data = {
                "message": "User registered successfully",
                "data": serializer.data,
                "errors": errors
            }
            response_status = status.HTTP_201_CREATED

        else:
            response_data = {
                "data" : None,
                "errors" : serializer.errors,
            }
            response_status = status.HTTP_400_BAD_REQUEST

        return Response(response_data,status=response_status)


class AccountLogin(generics.CreateAPIView):
    serializer_class = LoginSerializer
    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                response_data = {
                    "message": "logged-in successfully",
                    "data": serializer.data,
                    "errors": serializer.errors,
                }
                response_status = status.HTTP_200_OK

            else:

                response_data = {
                    "message": "invalid credentials",
                    "data": serializer.data,
                    "errors": serializer.errors,
                }
                response_status = status.HTTP_400_BAD_REQUEST

            return Response(response_data, status=response_status)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)