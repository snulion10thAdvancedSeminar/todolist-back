from inspect import trace
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics, serializers, status, views, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import SignUpSerializer, LoginSerializer, LogoutSerializer

class SignUpAPIView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        data = { "msg": "user created" }
        return JsonResponse(data, status=status.HTTP_201_CREATED)

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = { "msg": "token encoded" }
        access_token = serializer.data["tokens"]["access"]
        refresh_token = serializer.data["tokens"]["refresh"]
        res = JsonResponse(data, status=status.HTTP_200_OK)
        res.set_cookie('access_token', access_token)
        res.set_cookie('refresh_token', refresh_token)
        return res

class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = { "msg": "logout success" }
        res = JsonResponse(data, status=status.HTTP_200_OK)
        res.set_cookie('access_token', '')
        res.set_cookie('refresh_token', '')
        return res
