from unicodedata import category
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, User
from .models import Location, List, Product, Category, User, Tag

admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(List)
admin.site.register(Tag)
admin.site.register(User, UserAdmin)
