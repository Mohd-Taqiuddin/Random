from django.http import HttpResponse
from . import urls
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def addEvent(request):
    return render(request, 'add_event.html')