from django.shortcuts import render
from rest_framework import generics
from .models import User, Location, Category, Product, List
from .serializers import ListSerializer, UserSerializer
from rest_framework.generics import RetrieveDestroyAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

class DeleteList(RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    
class CreateList(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class AddListItem(RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class UpdateListItem(UpdateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer


class Register(CreateAPIView):
    serializer_class = UserSerializer