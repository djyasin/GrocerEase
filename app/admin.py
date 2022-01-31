from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, User
from .models import  List, User, Tag, ListItem

admin.site.register(List)
admin.site.register(Tag)
admin.site.register(ListItem)
admin.site.register(User, UserAdmin)
