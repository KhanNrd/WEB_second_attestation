from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.http import Http404
from .models import Person
from django.urls import reverse


def index(request):
    person_list = Person.objects.all
    return render(request,'contact/index.html',{'person_list':person_list})
def newperson(request):
    return render(request,'contact/newpersonform.html')
def add(request):
    name = request.POST['person_name']
    phone = request.POST['person_phone']
    photo = request.POST['person_photo']

    p = Person(person_name = name, person_phone = phone, person_photo = photo)
    p.save()
    return HttpResponseRedirect(reverse('contact:index'))
def edit(request,person_id):
    name = Person.objects.get(pk = person_id).person_name
    phone = Person.objects.get(pk = person_id).person_phone
    photo = Person.objects.get(pk = person_id).person_photo

    return render(request, 'contact/edit.html',{'name':name,'phone':phone,'photo':photo,'id':person_id})
def save(request, person_id):
    name = request.POST['person_name']
    phone = request.POST['person_phone']
    photo = request.POST['person_photo']
    Person.objects.filter(pk = person_id).update(person_name = name, person_phone = phone, person_photo = photo)
    return HttpResponseRedirect(reverse('contact:index'))

def delete(request, person_id):
    Person.objects.filter(pk = person_id).delete()
    return HttpResponseRedirect(reverse('contact:index'))
