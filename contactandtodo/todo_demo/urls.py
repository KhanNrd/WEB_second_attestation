from django.urls import path

from . import views
app_name = 'todo_demo'
urlpatterns = [
    path('',views.index, name = 'index'),
    path('todoitem/',views.TodoItemFunc, name = 'TodoItem'),
    path('add/',views.add,name = 'add'),
    path('<int:todo_id>/edit/',views.edit,name = 'edit'),
    path('save/',views.save,name = 'save'),
    path('<int:id>/delete/',views.delete,name = 'delete'),

]
