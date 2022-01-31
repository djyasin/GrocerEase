from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Tag(models.Model):
    tag = models.CharField(max_length=250)

class List(models.Model):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lists') 
    tags = models.ManyToManyField('Tag', related_name='lists', blank=True)
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
    ("FREEZER", "Frozen Goods")
)

    name = models.CharField(max_length=250)
    choices =  models.CharField(choices=CATEGORIES, max_length=100)
    item_quantity = models.PositiveIntegerField(default=1)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='list')