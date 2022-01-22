from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import User, Location, Category, Product, List, Tag, ListItem
from .serializers import ItemSerializer, ListSerializer, TagSerializer, UserSerializer
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class DeleteList(RetrieveDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    
class GroceryListView(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AddListItem(RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class UpdateList(UpdateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class CreateTag(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class ListItem(RetrieveUpdateDestroyAPIView):
    queryset = ListItem.objects.all()
    serializer_class = ItemSerializer

class CreateItem(generics.CreateAPIView):
    queryset = ListItem()
    serializer_class = ItemSerializer

class Lists(generics.ListAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class ViewLists(generics.ListAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

    def get_queryset(self):
        users = self.request.user
        queryset = List.objects.filter(users=users.pk)
        return queryset

