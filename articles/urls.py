from django.contrib import admin
from django.urls import path
from . import views 

app_name = 'articles'

urlpatterns = [
    path('', views.list_articles, name='articles_list'),
    path('<slug>/', views.article_detail, name='article_detail')
]