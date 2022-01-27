from random import choices
from sre_parse import CATEGORIES
from django.utils import timezone
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
    #isle_number
    pass

class Tag(models.Model):
    tag = models.CharField(max_length=250)

class Product(models.Model):
    name = models.CharField(max_length=250)
    image = models.URLField(max_length=200, null=True, blank=True)  
    locations = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='locations')


class List(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lists') 
    tags = models.ManyToManyField('Tag', related_name='lists', null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    
class ListItem(models.Model):
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

    name = models.CharField(max_length=250, null=True, blank=True)
    choices =  models.CharField(choices=CATEGORIES, max_length=100, null=True, blank=True)
    item_quantity = models.PositiveIntegerField(default=1)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='list')

