"""
URL configuration for name_projet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import index, other_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('other_page', other_page, name='other_page'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('add/', views.add_article, name='add_article'),
    path('delete/<int:pk>/', views.delete_article, name='delete_article'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
]
path('edit/<int:pk>/', views.edit_article, name='edit_article'),
