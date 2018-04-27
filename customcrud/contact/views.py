from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from contact.models import Contact
from contact.serializers import ContactSerializer


@csrf_exempt
def index(request):
    if request.method == "GET":
        contacts = Contact.objects.all()
        ser = ContactSerializer(contacts, many=True)
        return JsonResponse(ser.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        ser = ContactSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        return JsonResponse(ser.errors, status=400)


@csrf_exempt
def detail(request, contact_id):
    contact = Contact.objects.get(id=contact_id)

    if request.method=="GET":
        ser = ContactSerializer(contact)
        return JsonResponse(ser.data, status=200);
    elif request.method=="PUT":
        data = JSONParser().parse(request)
        ser = ContactSerializer(contact, data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data)
    elif request.method == "DELETE":
        contact.delete()
        ser = ContactSerializer(contact)
        return JsonResponse(ser.data)