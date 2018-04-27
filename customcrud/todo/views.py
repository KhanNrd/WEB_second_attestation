from django.shortcuts import render
from .models import Todo
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def index(request):
    if request.method == "GET":
        todos = Todo.objects.all()
        todo_json = [t.to_json() for t in todos]
        return JsonResponse(todo_json, safe=False)
    elif request.method == "POST":
        data = request.POST
        todo = Todo()
        todo.title = data.get('title', '')
        todo.body = data.get('body', '')
        todo.save()
        return JsonResponse(todo.to_json(), status=201, safe=True)

@csrf_exempt
def edit(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == "GET":
        return JsonResponse(todo.to_json(), safe=False)
    if request.method == "DELETE":
        todo.delete()
        return JsonResponse(todo.to_json(), safe=False)
    if request.method == "PUT":
        body = QueryDict(request.body)
        todo.isDone = body.get('isDone', todo.isDone)
        todo.body = body.get('body', todo.body)
        todo.title = body.get('title', todo.title)
        print(todo.isDone)
        todo.save()
        return JsonResponse(todo.to_json(), safe=False)
