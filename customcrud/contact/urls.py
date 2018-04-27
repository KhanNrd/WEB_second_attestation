from django.contrib import admin
from django.urls import path, include
from contact import views

urlpatterns = [
    path('contacts/', views.index),
    path('contacts/<int:contact_id>/', views.detail)
]
