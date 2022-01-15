from unicodedata import category
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django_toggle_m2m.toggle import ToggleManyToMany

class User(AbstractUser):
    following = models.ManyToManyField("CustomUser", related_name='followers', blank=True)

    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Location(models.Model):
    pass

class Category(models.Model):
    pass

class Product(models.Model):
    name = models.Charfield(max_length=250)
    image = models.URLField(max_length=200, null=True, blank=True)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    product_location = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='locations')

    # List
    # Users
    # Many to many
    # Product
    # Many to many
    # Slug
    # SlugField
    # (I think I need this for when users click a specific list)
    # Category:
    # Product_Categories
    # Foreign_key?

class List(models.Model):
    pass

