from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # User index
    path('', views.UserIndex.as_view(), name='index'),
    # User register
    path('', views.UserRegister.as_view(), name='register'),
    # User login
    path('', views.UserLogin.as_view(), name='login'),
    # User logout
    path('', views.UserLogout.as_view(), name='logout'),
]