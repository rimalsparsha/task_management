from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import UserCreateSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to register


class CustomTokenObtainPairView(TokenObtainPairView):
    # You can customize the token response here if needed
    pass