from django.contrib import admin
from django.urls import path
import webApp.views as views

urlpatterns = [
    path('', views.hello_world, name="hello_word"),
]