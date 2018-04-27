from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.http import Http404
from .models import Status,TodoItem
from django.urls import reverse
# Create your views here.
def index(request):
    todo_list = TodoItem.objects.all
    return render(request,'todo_demo/index.html',{'todo_list':todo_list})

def TodoItemFunc(request):
    return render(request,'todo_demo/TodoItem.html',{'statusList':Status.objects.all})

def add(request):
    text = request.POST['todo_text']
    status = request.POST['status']
    s = Status.objects.get(pk = status)
    todoItem = s.todoitem_set.create(todo_text = text)
    return HttpResponseRedirect(reverse('todo_demo:index'))

def edit(request, todo_id):
    text = TodoItem.objects.get(pk = todo_id).todo_text
    status = TodoItem.objects.get(pk = todo_id).todo_status

    Status.objects.get(pk = status.id).todoitem_set.get(pk = todo_id).delete()
    return render(request, 'todo_demo/edit.html',{'text':text,'status':status,'id':todo_id,'statusList':Status.objects.all})

def save(request):
    text = request.POST['todo_text']
    status = request.POST['status']
    s = Status.objects.get(pk = status)
    todoItem = s.todoitem_set.create(todo_text = text)
    return HttpResponseRedirect(reverse('todo_demo:index'))
def delete(request,id):
    
    return HttpResponseRedirect(reverse('todo_demo:index'))
