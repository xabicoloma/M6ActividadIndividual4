from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import *

urlpatterns = [
    path('', views.bienvenida, name='blog-home'),
    path('logIn/', views.logIn, name='logIn-home'),
    path('logOut/', views.logOut, name='logOut-home'),
    path('registro/', views.registro, name='registro-home'),
    path('mostrarUsuario/', mostrarUsuario, name='mostrarUsuario-home'),
]