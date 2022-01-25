from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import User, Location, Category, Product, List, Tag, ListItem
from .serializers import ItemSerializer, ListSerializer, TagSerializer, UserSerializer
from rest_framework.generics import ListAPIView, DestroyAPIView, ListCreateAPIView, RetrieveDestroyAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404

class GroceryListView(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ListDetailView(RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class UpdateListView(UpdateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class DeleteListView(DestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class CreateTagView(CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class ListItemsView(ListCreateAPIView):
    queryset = ListItem.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(list_id=self.kwargs["list_pk"])

    def perform_create(self, serializer):
        list = get_object_or_404(List, pk=self.kwargs["list_pk"])
        if self.request.user != list.user:
            raise PermissionDenied
        # if user does not own the list then return 403
        serializer.save(list=list)

class ListItemsDetailView(UpdateAPIView):
    queryset = ListItem.objects.all()
    serializer_class = ItemSerializer



# class AddListItemView(RetrieveUpdateDestroyAPIView):
#     queryset = List.objects.all()
#     serializer_class = ListSerializer

# class CreateItemView(generics.CreateAPIView):
#     queryset = ListItem()
#     serializer_class = ItemSerializer

# class ListsView(generics.ListAPIView):
#     queryset = List.objects.all()
#     serializer_class = ListSerializer

# class ViewListsView(generics.ListAPIView):
#     queryset = List.objects.all()
#     serializer_class = ListSerializer

#     def get_queryset(self):
#         users = self.request.user
#         queryset = List.objects.filter(users=users.pk)
#         return queryset



