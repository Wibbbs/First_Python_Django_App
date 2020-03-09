from django.contrib import admin
from django.urls import path
from . import views 

app_name = 'b2caudit'

urlpatterns = [
    path('', views.getAuditLog, name='getAuditLog'),
]