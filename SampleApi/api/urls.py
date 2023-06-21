from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData, name='get'),
    path('add/', views.addItem),
]
