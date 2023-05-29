from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer,UserLoginSerializer,UserProfileSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import User

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        message = {
            'message': 'hello world'
        }
        return Response(message)


class RegisterApiView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.create(serializer.validated_data)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user).data,
            "token": token.key
        })


class LoginApiView(APIView):
    def post(self,request):
        ser_data = UserLoginSerializer(data=request.data)
        if ser_data.is_valid():
            user = authenticate(phone_number=request.data.get('phone_number'),password=request.data.get('password'))
            if user is not None:
                login(request, user)
                token = Token.objects.get(user=user)
                return Response({"token": token.key})
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileApiView(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self,request):
        user = request.user
        return Response({"user": UserProfileSerializer(user).data})
