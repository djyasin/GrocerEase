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
        fields = ( 'products',
        'item_quantity',
        'list'
        )

class ListSerializer(serializers.ModelSerializer):

    class Meta:
        model = List
        fields = ('name',
        'users',
        'tags',
        'date_created'
        )

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ("username", "email", "password")

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user