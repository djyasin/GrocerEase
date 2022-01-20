from django.shortcuts import render
from rest_framework import generics
from .models import User, Location, Category, Product, List, Tag, ListItem
from .serializers import ItemSerializer, ListSerializer, TagSerializer, UserSerializer, RegisterSerializer
from rest_framework.generics import RetrieveDestroyAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class DeleteList(RetrieveDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    
class CreateList(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class AddListItem(RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class UpdateList(UpdateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class CreateTag(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class ListItem(RetrieveUpdateDestroyAPIView):
    queryset = ListItem()
    serializer_class = ItemSerializer

class CreateItem(generics.CreateAPIView):
    queryset = ListItem()
    serializer_class = ItemSerializer
