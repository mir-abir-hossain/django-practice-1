from django.contrib import admin
from django.urls import path
from . import views

app_name = "webapp"

urlpatterns = [
    path('home/', views.home, name="home"),
    path('aboutus/', views.aboutus, name="aboutus"),
]