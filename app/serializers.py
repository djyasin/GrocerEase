from rest_framework import serializers
from .models import User, Location, Category, Product, List

# class LoctaionSerializer(serializers.ModelSerializer):
#     pass

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('category')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name',
        'image',
        'categories',
        'locations'       
        )

class ListSerializer(serializers.ModelSerializer):

    class Meta:
        model = List
        fields = ('name',
        'users',
        'products'
        )

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ("username", "email", "password")