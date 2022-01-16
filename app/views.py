from django.shortcuts import render
from rest_framework import generics
from .models import User, Location, Category, Product, List
from .serializers import ListSerializer 
from rest_framework.generics import RetrieveAPIView,  CreateAPIView, ListCreateAPIView, ListAPIView, RetrieveDestroyAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

class CreateList(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer