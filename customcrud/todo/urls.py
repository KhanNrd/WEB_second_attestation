from django.contrib import admin
from django.urls import path, include
from todo import views

urlpatterns = [
    path('todos/', views.index),
    path('todos/<int:todo_id>', views.edit)
]
