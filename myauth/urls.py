from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path
from .views import login_view

app_name='myauth'

urlpatterns = [
  path('login/', LoginView.as_view(template_name="myauth/login.html"), name='login' ),
]