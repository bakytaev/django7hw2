"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from some_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/categories/', views.CategoryListCreateAPIView.as_view()),
    path('api/categories/list/', views.category_list),
    path('api/categories/<int:pk>/', views.category_detail),
    path('api/items/', views.ItemListCreateAPIView.as_view()),
    path('api/items/list/', views.item_list),
    path('api/items/<int:pk>/', views.item_detail),
]
