"""grocerease URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import include
from app import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('grocerease/lists/', app_views.GroceryListView.as_view(), name='lists'),
    path('grocerease/list_detail/<int:pk>/', app_views.ListDetailView.as_view(), name='list_detail'),
    path('grocerease/edit_list/<int:pk>/', app_views.UpdateListView.as_view(), name='edit_list'),
    path('grocerease/delete_list/<int:pk>/', app_views.DeleteListView.as_view(), name='delete_list'),
    path('grocerease/create_tag/', app_views.CreateTagView.as_view(), name='create_Tag'),
    path('grocerease/lists/<int:list_pk>/items/', app_views.ListItemsView.as_view(), name='list_items'),
    path('grocerease/item_detail/<int:pk>/', app_views.ListItemsDetailView.as_view(), name='item_detail'),
    
    

    # path('grocerease/create_item/', app_views.CreateItemView.as_view(), name='create_item'),
    # path('grocerease/view_lists/<int:pk>/', app_views.ViewListsView.as_view(), name='view_lists'),


    
]