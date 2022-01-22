from rest_framework import serializers
from .models import User, Location, Category, Product, List, Tag, ListItem
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

# class LoctaionSerializer(serializers.ModelSerializer):
#     pass

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag',)

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('category',)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name',
        'image',
        'categories',      
        )

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ListItem
        fields = ( 'pk',
        'products',
        'item_quantity',
        'list',
        'name'
        )

class ListSerializer(serializers.ModelSerializer):

    class Meta:
        model = List
        fields = ('pk',
        'name',
        'user', 
        'tags',
        'date_created'
        )
        read_only_fields = ['user']
        
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ("username", "email", "password")

