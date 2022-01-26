from random import choices
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.forms import ChoiceField
from rest_framework import serializers
from .models import User, Location, Product, List, Tag, ListItem
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import PermissionDenied
# class LoctaionSerializer(serializers.ModelSerializer):
#     pass

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag',)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name',
        'image',    
        )

class Categories(object):
    def __init__(self, choices): 
        self.choices = choices 

CATEGORIES = (
    ("PRODUCE", "Produce"),
    ("DAIRY", "Dairy"),
    ("BAKED", "Baked Goods"),
    ("MEAT", "Meat and Fish"),
    ("SNACKS", "Snacks"),
    ("ALCOHOL", "Alcohol"),
    ("BABY", "Baby Care"),
    ("CANNED", "Canned Goods"),
    ("DRY", "Dry Goods"),
    ("SAUCES", "Sauces and  Condiments"),
    ("HERBS", "Herbs and Spices"),
    ("BEVERAGES", "Non-Alcoholic Beverages"),
    ("HOUSEHOLD", "Household and Cleaning"),
    ("HEALTH", "Health and Beauty"),
    ("PET", "Pet Care"),
)

class ItemSerializer(serializers.ModelSerializer):
    choices = serializers.ChoiceField(choices = CATEGORIES) 


    class Meta:
        model = ListItem
        fields = ( 'pk',
        'list',
        'name',
        'item_quantity',
        'choices',
        )
        read_only_fields = ['list', 'choices']
    def to_representation(self, value):
        # sample: 'get_XXXX_display'
        method_name = 'get_{CATEGORIES}_display'.format(choices=self.choices)
        # retrieve instance method
        method = getattr(value, method_name)
        # finally use instance method to return result of get_XXXX_display()
        return method()

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

