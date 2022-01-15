from unicodedata import category
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django_toggle_m2m.toggle import ToggleManyToMany

class User(AbstractUser):

    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Location(models.Model):
    # number = models.IntegerField(Holding off on this for the moment.)
    #grocery_store = models.Charfield(max_length=250)
    pass

class Category(models.Model):
    category =  models.CharField(max_length=250)


class Product(models.Model):
    name = models.CharField(max_length=250)
    image = models.URLField(max_length=200, null=True, blank=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    locations = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='locations')

class List(models.Model):
    name = models.CharField(max_length=250)
    users = models.ManyToManyField('User', related_name='lists', blank=True)
    products = models.ManyToManyField('Product', related_name='products', blank=True)  
    # Slug
    # SlugField
    # (I think I need this for when users click a specific list, but not sure. Holding that for now.)

