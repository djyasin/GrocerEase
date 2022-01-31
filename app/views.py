from rest_framework import generics
from .models import List, Tag, ListItem
from .serializers import ItemSerializer, ListSerializer, TagSerializer
from rest_framework.generics import DestroyAPIView, ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404


class GroceryListView(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer


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
    queryset = ListItem.objects.all().order_by("choices")
    serializer_class = ItemSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ItemSerializer(queryset, many=True)
        categories = [cat for _, cat in ListItem.CATEGORIES]
        sorted_data = sorted(serializer.data,key=lambda item: categories.index(item['choices']))
        return Response(sorted_data)
        
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(list_id=self.kwargs["list_pk"])

    def perform_create(self, serializer):
        list = get_object_or_404(List, pk=self.kwargs["list_pk"])
        if self.request.user != list.user:
            raise PermissionDenied
        # if user does not own the list then return 403
        serializer.save(list=list)

class ItemDetailView(UpdateAPIView):
    queryset = ListItem.objects.all()
    serializer_class = ItemSerializer

class ItemDeleteView(DestroyAPIView):
    queryset = ListItem.objects.all()
    serializer_class = ItemSerializer


