from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, resolve
from .views import login_view

app_name='myauth'

urlpatterns = [
  path('login/', login_view, name='login' ),
]