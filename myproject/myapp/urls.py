from django.urls import path
from . import views

urlpatterns = [
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
    path('', views.article_list, name='article_list'),
    path('article/new/', views.article_create, name='article_create'),
    path('article/<int:pk>/delete/', views.article_delete, name='article_delete'),
]
