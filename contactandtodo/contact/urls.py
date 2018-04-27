from django.urls import path

from . import views
app_name = 'contact'

urlpatterns = [
    path('',views.index, name = 'index'),
    path('newperson/',views.newperson, name = 'newperson'),
    path('add/',views.add,name = 'add'),
    path('<int:person_id>/edit/',views.edit,name ='edit'),
    path('<int:person_id>/save/',views.save,name = 'save'),
    path('<int:person_id>/delete/',views.delete,name = 'delete'),

]
