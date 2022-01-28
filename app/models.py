# from sre_parse import CHOICES
from django.utils import timezone
# from unicodedata import choices
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
    name = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lists') 
    tags = models.ManyToManyField('Tag', related_name='lists', blank=True)
    date_created = models.DateTimeField(default=timezone.now)

class Choices(models.Model):
    PRODUCE = '1'
    DAIRY = '2'
    BAKED = '3'
    MEAT = '4'
    SNACKS = '5'
    ALCOHOL= '6'
    BABY = '7'
    CANNED = '8'
    DRY = '9'
    SAUCES = '10'
    HERBS = '11'
    BEVERAGES = '12'
    HOUSEHOLD = '13'
    HEALTH = '14'
    PET = '15'
    FREEZER = '16'

    CHOICES = (
        (PRODUCE, '1'),
        (DAIRY, '2'),
        (BAKED, '3'),
        (MEAT, '4'),
        (SNACKS, '5'),
        (ALCOHOL, '6'),
        (BABY, '7'),
        (CANNED, '8'),
        (DRY, '9'),
        (SAUCES, '10'),
        (HERBS, '11'),
        (BEVERAGES, '12'),
        (HOUSEHOLD,'13'),
        (HEALTH, '14'),
        (PET, '15'),
        (FREEZER, '16'),
    )
    status = models.CharField(
        max_length=42,
        choices=CHOICES,
        default= 1,
    )
class ListItem(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    choices =  models.ForeignKey(Choices, on_delete=models.CASCADE, related_name='choices')
    item_quantity = models.PositiveIntegerField(default=1)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='list')