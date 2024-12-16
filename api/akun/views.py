from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import *
from .models import *
from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate
from knox.models import AuthToken

User = get_user_model()
# Create your views here.

class LoginViewset(viewsets.ViewSet):
  permission_classes = [permissions.AllowAny]
  serializer_class = LoginSerializer

  def create(self, request):
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      email = serializer.validated_data['email']
      password = serializer.validated_data['password']
    
      user = authenticate(request, email=email, password=password)
      if user:
        _, token=AuthToken.objects.create(user)
        return Response(
          {
            "user": self.serializer_class(user).data,
            "token": token
          }
        )
      else:
        return Response({"error": "Invalid credentials"}, status=401)
    else:
      return Response(serializer.errors, status=400)

class RegisterViewSet(viewsets.ViewSet):
  permission_classes = [permissions.AllowAny]
  queryset = User.objects.all()
  serializer_class = RegisterSerializer

  def create(self,request):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=400)
    
class DistribusiViewset(viewsets.ViewSet):
  permission_classes = [permissions.AllowAny]
  queryset = penerima.objects.all()
  serializer_class = DistribusiPenerima

  def create(self,request):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=400)
    
  def list(self, request):
    queryset = self.queryset
    serializer = self.serializer_class(queryset, many=True)
    return Response(serializer.data)
  
  def retrieve(self, request, pk=None):
    regpenerima = self.queryset.get(pk=pk)
    serializer = self.serializer_class(regpenerima)
    return Response(serializer.data)
    
  def destroy(self, request, pk=None):
    regpenerima = self.queryset.get(pk=pk)
    regpenerima.delete()
    return Response(status=204)
  
class ZakatViewset(viewsets.ViewSet):
  permission_classes = [permissions.AllowAny]
  queryset = zakat.objects.all()
  serializer_class = BayarZakat

  def create(self,request):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=400)
    
  def list(self, request):
    queryset = self.queryset
    serializer = self.serializer_class(queryset, many=True)
    return Response(serializer.data)
  
  def retrieve(self, request, pk=None):
    regzakat = self.queryset.get(pk=pk)
    serializer = self.serializer_class(regzakat)
    return Response(serializer.data)
    
  def destroy(self, request, pk=None):
    regzakat = self.queryset.get(pk=pk)
    regzakat.delete()
    return Response(status=204)
  
    
class RegisterAmilViewSet(viewsets.ViewSet):
  permission_classes = [permissions.AllowAny]
  queryset = amil.objects.all()
  serializer_class = AmilSerializer

  def create(self,request):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=400)
    
  def list(self, request):
    queryset = self.queryset
    serializer = self.serializer_class(queryset, many=True)
    return Response(serializer.data)
  
  def retrieve(self, request, pk=None):
    regamil = self.queryset.get(pk=pk)
    serializer = self.serializer_class(regamil)
    return Response(serializer.data)
    
  def destroy(self, request, pk=None):
    regamil = self.queryset.get(pk=pk)
    regamil.delete()
    return Response(status=204)
  